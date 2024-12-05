# request digunakan untuk melakukan penggunaan metode HTTP seperti GET, POST, dll
from flask import Flask, render_template, request
# tensorflow.keras library untuk praproses
from tensorflow.keras.preprocessing.image import load_img, img_to_array
# tensorflow.keras library untuk menggunakan pretrained model
from tensorflow.keras.models import load_model
# untuk perhitungan komputasi
import numpy as np
# untuk regex pada string
import re
import base64
from io import BytesIO
from PIL import Image

# direktori model berada
loaded_model = load_model("models/model_fixx.h5")
print('Model ready!!')

# inisialisasi flask
app = Flask(__name__)


# Decoding an image from base64 and converting to NumPy array
def decode_image(imgData):
    imgstr = re.search(r'base64,(.*)', str(imgData)).group(1)
    img_bytes = base64.b64decode(imgstr)
    img = Image.open(BytesIO(img_bytes)).convert("RGB")  # Buka gambar di memori
    img = img.resize((150, 150))  # Sesuaikan ukuran gambar dengan model
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalisasi
    return img_array

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict/', methods=['POST'])
def predict():
    class_names = [ 'a\'in', 'alif', 'ba', 'dal', 'dhod', 'dzal',
                'dzo', 'fa', 'gho\'in', 'ha', 'hamzah', 'jim',
                'kaf', 'kha', 'kho', 'lam', 'lamalif', 'mim', 'nun', 'qof',
                'ro', 'shod', 'sin', 'syin', 'ta', 'tho', 'tsa', 
                'waw', 'ya', 'zain']
    # Ambil data base64 dari request
    imgData = request.get_data()

    # Decode gambar langsung dari base64 ke array
    img_array = decode_image(imgData)

    # melakukan prediksi
    pred = loaded_model.predict(img_array)
    print(pred)
    print(class_names[np.argmax(pred)])
    # konversi respon menjadi string
    response = class_names[np.argmax(pred)]
    return str(response)


if __name__ == "__main__":
    # run the app locally 
    app.run(app.run(debug=False, host='0.0.0.0'))