import tensorflow as tf
from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.preprocessing.image import load_img , img_to_array
import numpy as np
import cv2
print(tf.__version__)
model = model_from_json(open("res.json", "r").read())
#load weights
model.load_weights('res.h5')
file_path1 = "C:/Users/HP/OneDrive/Pictures/Screenshots/Screenshot (37).png"
file_path2 = "C:/Users/HP/OneDrive/Pictures/Screenshots/Screenshot (32).png"
img = cv2.imread(file_path1)
imgnew = cv2.resize(img, (200, 200), 3)

imgnew = img_to_array(imgnew)
imgnew = np.expand_dims(imgnew, axis=0)

preds = model.predict(imgnew)[0]
output = np.argmax(preds)
count = output
img1 = cv2.imread(file_path2)
imgnew1 = cv2.resize(img1, (200, 200), 3)

imgnew1 = img_to_array(imgnew1)
imgnew1 = np.expand_dims(imgnew1, axis=0)

preds1 = model.predict(imgnew1)[0]
output1 = np.argmax(preds1)
print(output,output1)