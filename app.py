from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from PIL import Image #use PIL
import numpy as np

app = Flask(__name__)

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
    if pred = 0:
        return(render_template("index.html", result="You may have Actinic Keratosis which has a  small risk of cancer. Please continue monitoring for changes."))
    elif pred = 1:
        return(render_template("index.html", result="You may have Basal Cell Carcinoma (Cancerous). It is  reccommended to consult a dermatologist as soon as possible. ")) 
    elif pred = 2:
        return(render_template("index.html", result="Your skin lesion is non-cancerous. Please continue monitoring for changes."))
    elif pred = 3:
        return(render_template("index.html", result="Your skin lesion is non-cancerous. Please continue monitoring for changes."))
    elif pred = 4:
        return(render_template("index.html", result="Your skin lesion is non-cancerous. Please continue monitoring for changes."))
    elif pred = 5:
        return(render_template("index.html", result="You may have Vascular Lesions which has a small risk of cancer. Please continue monitoring for changes."))
    elif pred = 6:
        return(render_template("index.html", result="You may have Melanoma (Cancerous). It is  reccommended to consult a dermatologist as soon as possible. ")) 
    else:
        return(render_template("index.html", result="Pending Upload"))
if __name__ == "__main__":
    app.run()


# In[ ]:


if __name__=="__main__":
    app.run()


# https://towardsdatascience.com/image-classification-of-pcbs-and-its-web-application-flask-c2b26039924a
