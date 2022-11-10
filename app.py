from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from PIL import Image #use PIL
import numpy as np


app = Flask(__name__)


def msg(pred):
    labels = {0 : "Actinic Keratos. Low risk of cancer, please continue to monitor.",
              1 : "Cancerous: Basal Cell Carcinoma. Consult a dermatologist as soon as possible. ",
              2 : "Benign Keratosis. You are safe.",
              3 : "Dermatofibroma. You are safe.",
              4 : "Melanocytic Nevi. You are safe.",
              5 : "Vascular Lesion. Low risk of cancer, please continue to monitor.",
              6 : "Cancerous: Melanoma. Consult a dermatologist as soon as possible." }

    if pred in labels:
        return(str(labels[pred])) 
    else:
        return(str("Please upload an image."))
    
@app.route('/', methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        file = request.files['file']
        print("File Received")
        filename = secure_filename(file.filename)
        print(filename)
        # Open the image form working directory
        image = Image.open(file)
        model = load_model("SkinCancer")
        img = np.asarray(image)
        img.resize((150,150,3))
        img = np.asarray(img, dtype="float32") #need to transfer to np to reshape
        img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2]) #rgb to reshape to 1,100,100,3
        pred=model.predict(img)
        pred=np.argmax(pred,axis=1)
        pred = int(pred)
        results = msg(pred)
        print(results)
        
        return(render_template("index.html", result=results))
    else:
        return(render_template("index.html", result="Pending Upload"))
        
if __name__ == "__main__":
    app.run()
# In[ ]:
if __name__=="__main__":
    app.run()
