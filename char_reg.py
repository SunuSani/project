import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
#Define Path
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
#Load the pre-trained models
model = load_model(model_path)
model.load_weights(model_weights_path)
#Define image parameters
img_width, img_height = 150, 150
class_value=['(', ')', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&=', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', 'a', 'b', 'c', 'd', '\div', 'e', 'f', 'g', 'gt', 'h', 'i', 'j', 'k', 'l', 'lt', 'm', '/ast', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Prediction Function
def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  result = array[0]
  answer = np.around(array, decimals=3)
  answer = np.argmax(answer)
  r=class_value[answer]	
  return r
