import cv2
import numpy as np
import face_recognition
from PIL import Image

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while True:
    tet, img = cap.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resize = cv2.resize(rgb, (0, 0), fx=0.5, fy=0.5)

    boxes = face_recognition.face_locations(resize, model="cnn")
    print(boxes)
    #gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(faces)

#[(81, 183, 129, 135)]
# [[131  71  65  65]]

    for (x, y, w, h) in boxes:
        cv2.rectangle(resize, (h, x), (y, w), (255, 0, 0), 2)
        # cv2.rectangle(img,(x,y),(x-30,y-6),(255,255,255),2)
        #roi_gray = gray[y:y+h, x:x+w]
        roi_color = resize[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #	cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0),2)
    cv2.imshow('img', resize)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
