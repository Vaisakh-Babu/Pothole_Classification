from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import matplotlib.pyplot as plt
from keras.preprocessing import image
import os

import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("my_model_potholes")

class_dict = {0:'normal', 1:"potholes"}


img = ''
result = ''

app = Flask(__name__)


@app.route('/')
def upload():
    try:
        os.remove("static/*")
    except:
        None

    return """
<html>
   <body>
      <form action = "http://localhost:5000/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
   </body>
</html>
"""



@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    try:
        os.remove("static/*")
    except:
        None
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        global img
        global result
        img = image.img_to_array(image.load_img(f.filename, target_size=(64,64)))
        plt.imshow(image.load_img(f.filename, target_size=(200,200)))
        plt.axis("off")
        # plt.show()
        plt.savefig("static/" + f.filename,)
        test_images = [img]
        test_images = np.asarray(test_images)
        test_images = test_images * (1/255)
        val = model.predict(test_images)
        result = class_dict[1 if val[0] > 0.5 else 0]
        
#         print(f"Prediction : {result}") # class_dict[val]
#         return render_template("show.html", data = ["/home/vb/Documents/Aegis/Deep Learning/Project/static" + f.filename, result])
        return render_template("show.html", data = ["../static/" + f.filename, result])
if __name__ == '__main__':
    app.run()
