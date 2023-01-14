from flask import Flask, request, jsonify
from keras_preprocessing import image
from PIL import Image
import numpy as np
from tensorflow import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model = keras.models.load_model("model/CXR.h5")

class_type = {0: 'Covid', 1: 'Normal'}


def pre_process_image(img_path):
    path = img_path
    img = image.load_img(path, target_size=(224, 224, 3))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img
    
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        filename = request.files.getlist('file')
        print(request.files)
        print(filename)

        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            pillow_img = Image.open(file)
            pillow_img = pillow_img.save("upload/given.png")
            img = pre_process_image("upload/given.png")
            covid = model.predict(img)[0][0]*100
            normal = model.predict(img)[0][1]*100
            if(covid > normal):
                prediction = "Covid"
            else:
                prediction = "Normal"
            data = prediction
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})
    return "Covid server"

if __name__ == "__main__":
    app.run(debug=True)

