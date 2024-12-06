Arabic Character Recognition with Flask and TensorFlow
This is a Flask-based web application for recognizing Arabic characters using a Convolutional Neural Network (CNN) model built with TensorFlow/Keras. The application takes an image as input and predicts the corresponding Arabic character.

Features
Deep Learning: Uses a pre-trained CNN model for predictions.
Web Interface: Simple web interface built with Flask and HTML templates.
Base64 Image Decoding: Processes image inputs directly from Base64 strings.

Prerequisites
Python 3.7 or higher
Pip for managing Python packages
Installation
Clone the repository:

bash
Salin kode
git clone https://github.com/yourusername/arabic-character-recognition.git
cd arabic-character-recognition
Create and activate a virtual environment:

bash
Salin kode
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
Salin kode
pip install -r requirements.txt
Ensure the pre-trained model (model_fixx.h5) is in the models/ directory.

Running the Application
Start the Flask development server:

bash
Salin kode
flask run
Access the application in your web browser at:

arduino
Salin kode
http://127.0.0.1:5000/
Use the interface to upload an image of an Arabic character and see the prediction.

CNN Model Details
The CNN model is trained to recognize 30 Arabic characters, including:

a'in, alif, ba, dal, dhod, dzal, ... , zain

Input Preprocessing
Images are resized to 150x150 pixels.
Images are normalized (pixel values divided by 255).
Troubleshooting
If the server fails to start, ensure all dependencies are installed and the Python version is compatible.
Check the models/ directory for the presence of the model_fixx.h5 file.
