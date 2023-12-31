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

# direktori model berada
loaded_model = load_model("models/model_fixx.h5")
print('Model ready!!')

# inisialisasi flask
app = Flask(__name__)

import base64


# decoding an image from base64 into raw representation
def convertImage(imgData):
    imgstr = re.search(r'base64,(.*)', str(imgData)).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))

# load image
def load_image(img_path):
    # Praproses data uji
    img = load_img(img_path, target_size=(150,150,3))
    img_tensor = img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.0
    

    return img_tensor

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    class_names = [ 'a\'in', 'alif', 'ba', 'dal', 'dhod', 'dzal',
                'dzo', 'fa', 'gho\'in', 'ha', 'hamzah', 'jim',
                'kaf', 'kha', 'kho', 'lam', 'lamalif', 'mim', 'nun', 'qof',
                'ro', 'shod', 'sin', 'syin', 'ta', 'tho', 'tsa', 
                'waw', 'ya', 'zain']
    # ketika tombol prediksi ditekan maka akan dilakukan sebuah proses konversi berdasarkan yang dituliskan oleh pengguna
    imgData = request.get_data()
    # encode menjadi sebuah output.png
    convertImage(imgData)
    # membaca gambar
    img = load_image('output.png')

    # melakukan prediksi
    pred = loaded_model.predict(img)
    print(pred)
    print(class_names[np.argmax(pred)])
    # konversi respon menjadi string
    response = class_names[np.argmax(pred)]
    return str(response)


if __name__ == "__main__":
    # run the app locally 
    app.run(app.run(debug=False, host='0.0.0.0'))