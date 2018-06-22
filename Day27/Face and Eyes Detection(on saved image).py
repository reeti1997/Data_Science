# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:18:30 2018

@author: reeti
"""

import cv2
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# Importing html smaples for Face and Eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Reading the given Image and converting it to Grayscale
img = cv2.imread('baby.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting Faces from image using Face_Samples
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Iterating for the dimentions of the Detected faces to draw rectangle
for (x,y,w,h) in faces:
    # Creating Rectangle around Face with color Red and of width 2
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Getting start and end points of face to detect eyes within the Face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # Detecting Eyes from image using Eye_Samples
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    # Iterating for the dimentions of the Detected Eyes to draw rectangle
    for (ex,ey,ew,eh) in eyes:
        # Creating Rectangle around Eyes with color Green and of width 2
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img) # Displays the Image with rectangles on Face and Eyes

k = cv2.waitKey(0)
stop = ord("S") # To Stop press capital S (While on the output image)
if k == stop:
    cv2.destroyAllWindows()

elif k == ord('q'):   # To Save and close press q
    cv2.imwrite('marked1.png',img)
    cv2.destroyAllWindows()