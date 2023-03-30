import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from PIL import ImageFile, Image
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50
ImageFile.LOAD_TRUNCATED_IMAGES = True

model = load_model("C:/Users/msi9/OneDrive/Desktop/Documents/universty reqiurement/native -app/flaskApp/backend/Qalamy.h5")

def getPrediction(img_bytes, model):
    # Loads the image and transforms it to (224, 224, 3) shape
   img=cv2.imread(img_bytes) 
   img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   img=cv2.resize(img,(32,32))
   img=img.reshape(-1,32,32,1)
   img=img/255
   preds=model.predict(img)
   return preds

def classifyImage(file):


    # Returns a probability scores matrix 
    preds = getPrediction(file, model)
    # Decode tha matrix to the following format (class_name, class_description, score) and pick the heighest score
    # We are going to use class_description since that describes what the model sees
    prediction =np.argmax(preds)
    # prediction[0][0][1] is eqaul to the first batch, top prediction and class_description
    
    return prediction