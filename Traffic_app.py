from flask import *
import os
import base64
from io import BytesIO
from werkzeug.utils import secure_filename

try:
    from tensorflow.keras.models import load_model
except ImportError:
    from keras.models import load_model

import numpy as np
from PIL import Image
import cv2
import time

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

app = Flask(__name__)

# =========================
# LOAD MODEL
# =========================
model = load_model('./model/TSR.h5')

# =========================
# GLOBAL VARIABLES
# =========================
last_prediction = None
last_prediction_time = 0
prediction_cooldown = 2.0  # seconds

# =========================
# TRAFFIC SIGN CLASSES
# =========================
classes = {
    0: 'Speed limit (20km/h)',
    1: 'Speed limit (30km/h)',
    2: 'Speed limit (50km/h)',
    3: 'Speed limit (60km/h)',
    4: 'Speed limit (70km/h)',
    5: 'Speed limit (80km/h)',
    6: 'End of speed limit (80km/h)',
    7: 'Speed limit (100km/h)',
    8: 'Speed limit (120km/h)',
    9: 'No passing',
    10: 'No passing veh over 3.5 tons',
    11: 'Right-of-way at intersection',
    12: 'Priority road',
    13: 'Yield',
    14: 'Stop',
    15: 'No vehicles',
    16: 'Vehicle > 3.5 tons prohibited',
    17: 'No entry',
    18: 'General caution',
    19: 'Dangerous curve left',
    20: 'Dangerous curve right',
    21: 'Double curve',
    22: 'Bumpy road',
    23: 'Slippery road',
    24: 'Road narrows on the right',
    25: 'Road work',
    26: 'Traffic signals',
    27: 'Pedestrians',
    28: 'Children crossing',
    29: 'Bicycles crossing',
    30: 'Beware of ice/snow',
    31: 'Wild animals crossing',
    32: 'End speed + passing limits',
    33: 'Turn right ahead',
    34: 'Turn left ahead',
    35: 'Ahead only',
    36: 'Go straight or right',
    37: 'Go straight or left',
    38: 'Keep right',
    39: 'Keep left',
    40: 'Roundabout mandatory',
    41: 'End of no passing',
    42: 'End no passing vehicle > 3.5 tons'
}

# =========================
# TEXT TO SPEECH
# =========================
def speak_prediction(text):
    if pyttsx3 is None:
        print(f"ALERT: {text}")
        return

    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)
        engine.setProperty('volume', 0.9)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"Voice alert failed: {e}")
        print(f"ALERT: {text}")

# =========================
# IMAGE PREDICTION
# =========================
def predict_image_pil(image):
    image = image.convert('RGB')
    image = image.resize((30, 30))
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array, verbose=0)
    class_id = int(np.argmax(predictions, axis=1)[0])
    confidence = float(np.max(predictions))
    class_name = classes.get(class_id, f"Unknown ({class_id})")

    return class_id, class_name, confidence

# =========================
# ROUTES
# =========================
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/detect')
def detect():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sign-classes')
def sign_classes():
    return render_template('sign_classes.html', classes=classes)

@app.route('/live-camera')
def live_camera():
    return render_template('live_camera.html')

# =========================
# PREDICT FROM UPLOADED FILE
# =========================
@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded"

        f = request.files['file']

        if f.filename == '':
            return "No selected file"

        file_path = secure_filename(f.filename)
        f.save(file_path)

        image = Image.open(file_path)
        class_id, class_name, confidence = predict_image_pil(image)

        result_text = f"Predicted Traffic🚦Sign is: {class_name} ({confidence:.2f})"

        speak_prediction(f"Traffic sign detected: {class_name}")

        os.remove(file_path)
        return result_text

    return None

# =========================
# LIVE CAMERA FRAME PREDICTION
# =========================
@app.route('/predict_frame', methods=['POST'])
def predict_frame():
    global last_prediction, last_prediction_time

    try:
        data = request.get_json()
        image_data = data.get("image", "")

        if not image_data:
            return jsonify({"status": "error", "message": "No image received"})

        # Remove base64 header
        if "," in image_data:
            image_data = image_data.split(",")[1]

        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes)).convert("RGB")

        class_id, class_name, confidence = predict_image_pil(image)

        should_speak = False
        current_time = time.time()

        if confidence >= 0.70:
            if (last_prediction != class_name or
                current_time - last_prediction_time > prediction_cooldown):
                last_prediction = class_name
                last_prediction_time = current_time
                should_speak = True
                speak_prediction(f"Traffic sign detected: {class_name}")

        return jsonify({
            "status": "success",
            "class_id": class_id,
            "class_name": class_name,
            "confidence": round(confidence, 2),
            "speak": should_speak
        })

    except Exception as e:
        print(f"Error in predict_frame: {e}")
        return jsonify({"status": "error", "message": str(e)})

# =========================
# MAIN
# =========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
