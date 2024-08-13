from tensorflow.keras.models import model_from_json
import cv2
import numpy as np
from PIL import Image,ImageTk,ImageDraw,ImageFont
import PIL
#import imquality.brisque as brisque

#from keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import img_to_array
#import matplotlib.pyplot as plt
model = model_from_json(open("res.json", "r").read())
#load weights
model.load_weights('res.h5')
#file_path1 = "C:/Users/HP/OneDrive/Desktop/signature.jpg"
#file_path2 = "C:/Users/HP/OneDrive/Desktop/photo.jpg"

#image quality checking
'''def imageQuality(file_path1):
    img = PIL.Image.open(file_path1)
    return brisque.score(img)'''


def check(file_path1, file_path2):
    print("In module")
    print(file_path1, file_path2)
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
    print(output1)
    count1 = output1
    print(count,count1)
    #return count, count1
    if (count == 0 and count1 == 0):
        # error_label=Label(window,text="INSERT ONLY ONE PHOTO",font=('Times 18'),width=30, height=1)
        print("INSERT ONLY ONE PHOTO")
        return "two", "photos"

        # error_label.place(x = 500, y =700)
    elif (count != 0 and count1 != 0):
        # error_label=Label(window,text="INSERT ONLY ONE SIGNATURE",font=('Times 18'),width=30, height=1)
        print("INSERT ONLY ONE SIGNATURE")
        return "two","signatures"
        # error_label.place(x = 500, y =700)
    elif (count != 0 and count1 == 0):
        # error_label=Label(window,text="Submitted Successfully",font=('Times 18'),width=30, height=1)
        print("Submitted successfully")
        # error_label.place(x = 500, y =700)
        return swap(file_path1,file_path2)
    elif (count == 0 and count1 != 0):
        # error_label=Label(window,text="Submitted Successfully",font=('Times 18'),width=30, height=1)
        print("Submitted Successfully")
        # error_label.place(x = 500, y =700)
        return display(file_path1,file_path2)
    # else:
    #    display()
    cv2.imwrite("face_detected.png", img)
    print(count)
    print('Successfully saved')
    print('Before Swapping:')
    print('photo: ' + file_path1)
    print('sign: ' + file_path2)
def swap(file_path1,file_path2):
    #function to swap locations of images
    '''global file_path1
    global file_path2'''
    file_path1,file_path2=file_path2,file_path1
    print('After Swapping:')
    print('photo: '+file_path1)
    print('sign: '+file_path2)
    #print(file_path1,file_path2)
    return display(file_path1,file_path2)


def display(file_path1,file_path2):

    print('Final photo: ' + file_path1)
    print('Final sign: ' + file_path2)
    return file_path1,file_path2
    photo = Image.open(file_path1)
    rload = photo.resize((250, 250))
    sign = Image.open(file_path2)
    rload2 = sign.resize((250, 250))

