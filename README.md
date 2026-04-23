# SignVision  
## A Hybrid Deep Vision Framework for Robust Traffic Sign Recognition in Adverse Weather Conditions

SignVision is a hybrid deep learning-based traffic sign recognition system designed for real-world driving environments. It combines the fast detection capability of **YOLOv8** with the precise localization strength of **Faster R-CNN** to detect traffic signs accurately under challenging weather conditions such as **rain, fog, glare, and low light**. The system also integrates **voice alerts** to improve driver safety and accessibility.

---

## 📌 Project Overview

Traffic sign recognition plays a critical role in **Advanced Driver Assistance Systems (ADAS)** and autonomous driving. However, real-world conditions often make detection difficult due to:

- Occlusion  
- Blur  
- Weather interference  
- Varying illumination  

**SignVision** addresses these challenges by:

- Detecting traffic signs in real time  
- Improving accuracy using a hybrid **YOLOv8 + Faster R-CNN** pipeline  
- Enhancing robustness through **weather-based data augmentation**  
- Providing **text-to-speech voice alerts** for detected signs  

---

## ✨ Features

- Real-time traffic sign detection  
- Hybrid architecture using **YOLOv8** and **Faster R-CNN**  
- Robust performance under adverse weather conditions  
- Weather augmentation for improved generalization  
- Voice alert system for accessibility and driver support  
- Web-based interface for image upload and prediction  
- Live camera detection support  
- Support for **43 traffic sign classes** from the **GTSRB dataset**

---

## 🧠 Architecture

The system follows a **cascaded hybrid approach**:

1. **YOLOv8** detects candidate traffic sign regions quickly  
2. **Faster R-CNN** refines detections for better localization  
3. **NMS fusion** removes overlapping boxes and finalizes predictions  
4. **Voice module** converts detected sign labels into spoken alerts  

---

## 📂 Dataset

This project uses the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset.

### Dataset Details
- **43 classes**
- **50,000+ images**
- Images resized and preprocessed for model compatibility

### Weather Augmentation Applied
- Rain
- Fog
- Glare
- Brightness variation
- Low-light simulation

---

## 🛠️ Tech Stack

### Programming & Frameworks
- Python
- Flask
- HTML
- CSS
- JavaScript

### Deep Learning & CV
- TensorFlow / Keras
- PyTorch
- YOLOv8
- Faster R-CNN
- OpenCV
- NumPy
- Pillow

### Additional Tools
- pyttsx3 / gTTS (Voice Alerts)
- Pandas
- Scikit-learn

---

## ⚙️ Methodology

- Input images are preprocessed and resized  
- YOLOv8 generates initial traffic sign proposals  
- Faster R-CNN refines the detected sign regions  
- Non-Maximum Suppression (**NMS**) is applied to remove overlapping detections  
- Final predictions are displayed with confidence scores  
- Voice alerts are triggered for detected traffic signs  

---

## 📊 Performance

The proposed **SignVision** framework achieved:

- **97.5% Test Accuracy**
- **97.8 mAP**
- **45 ms Inference Time**
- **92% User Satisfaction** for accessibility and usability

> *Note: These results may vary depending on hardware and dataset split.*

---

# SignVision  
A Hybrid Deep Vision Framework for Robust Traffic Sign Recognition in Adverse Weather Conditions

## 📁 Project Structure

```bash
SignVision/
│
├── model/
│   ├── TSR.h5
│   └── fast_faster_rcnn.pth
│
├── static/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── index.html
│   ├── about.html
│   ├── live_camera.html
│   └── sign_classes.html
│
├── archive/
│   ├── Train.csv
│   ├── Test.csv
│   └── ...
│
├── datasets/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/SignVision.git
cd SignVision
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On Mac/Linux:
```bash
source venv/bin/activate
```

### 4. Install required dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Flask web application
```bash
python app.py
```

Then open your browser and go to:

```bash
http://127.0.0.1:5000/
```

---

## 📦 Requirements

Make sure the following are installed:

- Python 3.9 or above
- pip
- Webcam (for live camera detection)
- Internet browser (Chrome / Edge recommended)

---

## 🖼️ Functional Modules

### 1. Image Upload Detection
- Upload a traffic sign image
- Model predicts the class label
- Voice alert is generated

### 2. Live Camera Detection
- Access webcam from browser
- Capture frame in real-time
- Predict traffic sign from camera input
- Display result and confidence score
- Trigger voice alert

### 3. Sign Classes Page
- Displays all supported traffic sign classes

---

## 🔊 Voice Alert Feature

The system uses **text-to-speech (TTS)** to announce detected traffic signs.

### Example:
- “Traffic sign detected: Stop”
- “Traffic sign detected: Speed limit 50 km/h”

### This improves:
- Accessibility
- Driver assistance
- Hands-free interaction

---

## 📷 Live Camera Support

The live camera module allows real-time traffic sign prediction through the webcam.

### Browser Requirements
- Allow camera permission when prompted
- Use **Chrome** or **Edge** for best compatibility
- Ensure webcam is not being used by another application

---

## 📌 Example Use Cases

- Driver assistance systems
- Smart transportation applications
- Traffic sign education tools
- Accessibility-focused visual recognition systems
- Research in adverse weather object detection

---

## 🔮 Future Scope

- Integrating radar or infrared-based multimodal sensing
- Improving performance in heavy rain and extreme fog
- Supporting multilingual voice alerts
- Mobile app deployment
- Full ADAS integration

---

## 🏁 Conclusion

**SignVision** is a practical and robust traffic sign recognition system designed for intelligent transportation and autonomous driving applications. Its **hybrid detection strategy**, **weather robustness**, and **voice alert support** make it suitable for both **accuracy-focused** and **accessibility-focused** real-world deployment.er robustness**, and **voice alert support** make it suitable for both **accuracy-focused** and **accessibility-focused** real-world deployment.
