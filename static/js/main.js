$(document).ready(function () {
    // Initialize elements
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    // File input change handler
    $("#imageUpload").change(function () {
        var file = this.files[0];
        if (file) {
            // Validate file type
            var validTypes = ['image/jpeg', 'image/jpg', 'image/png'];
            if (!validTypes.includes(file.type)) {
                alert('Please select a valid image file (JPEG, JPG, or PNG).');
                this.value = '';
                return;
            }

            // Validate file size (max 10MB)
            if (file.size > 10 * 1024 * 1024) {
                alert('File size must be less than 10MB.');
                this.value = '';
                return;
            }

            $('.image-section').show();
            $('#btn-predict').show();
            $('#result').hide();
            $('#result-text').text('');
            $('.upload-label').text('Change Image');
            readURL(this);
        }
    });

    // Prediction button click handler
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();
        $('#result').hide();

        // Disable file input during processing
        $('#imageUpload').prop('disabled', true);
        $('.upload-label').css('pointer-events', 'none');

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Hide loader and show result
                $('.loader').hide();
                $('#result-text').text(data);
                $('#result').fadeIn(600);

                // Re-enable file input
                $('#imageUpload').prop('disabled', false);
                $('.upload-label').css('pointer-events', 'auto');

                console.log('Prediction successful!');
            },
            error: function (xhr, status, error) {
                // Hide loader and show error
                $('.loader').hide();
                $('#btn-predict').show();

                // Re-enable file input
                $('#imageUpload').prop('disabled', false);
                $('.upload-label').css('pointer-events', 'auto');

                // Show error message
                $('#result-text').text('Error: Unable to process the image. Please try again.');
                $('#result .alert').removeClass('alert-success').addClass('alert-danger');
                $('#result').fadeIn(600);

                console.error('Prediction failed:', error);
            }
        });
    });

    // Smooth scrolling for anchor links
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if (target.length) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 70
            }, 1000);
        }
    });

    // Add some visual feedback for file drag and drop (optional enhancement)
    $('.upload-area').on('dragover dragenter', function() {
        $(this).addClass('drag-over');
    }).on('dragleave dragend drop', function() {
        $(this).removeClass('drag-over');
    });
});