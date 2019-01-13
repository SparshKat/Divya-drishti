import cv2
from PIL import Image
import os
import argparse
import imutils
import math
import numpy as np
from imutils.video import VideoStream
import face_recognition

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", type=str, required=False,
                help="Folder to save images")
ap.add_argument("-v", "--video", type=str,
                help="path to input video")

args = vars(ap.parse_args())
folder = args["folder"]
video_file = args["video"]
i = 1
cap = VideoStream(src=video_file).start()


path = os.getcwd()
path = os.path.join(path, "dataset")
os.chdir(path)
if folder in os.listdir():
    os.chdir(folder)
print(path)
if folder not in os.listdir():
    os.mkdir(folder)
    os.chdir(folder)

def rotate_image(mat, angle):
    height, width = mat.shape[:2]
    image_center = (width / 2, height / 2)

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)

    radians = math.radians(angle)
    sin = math.sin(radians)
    cos = math.cos(radians)
    bound_w = int((height * abs(sin)) + (width * abs(cos)))
    bound_h = int((height * abs(cos)) + (width * abs(sin)))

    rotation_mat[0, 2] += ((bound_w / 2) - image_center[0])
    rotation_mat[1, 2] += ((bound_h / 2) - image_center[1])

    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat

while True:
    img = cap.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = rotate_image(img, -90)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(img, width=750)
    r = img.shape[1] / float(rgb.shape[1])
    # r=1
    boxes = face_recognition.face_locations(rgb, model="cnn")
    print(boxes)
    #gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # print(faces)

#[(81, 183, 129, 135)]
# [[131  71  65  65]]

    for (top, right, bottom, left) in boxes:
        ''' w=(right-left)
         h=(top-bottom)
         x=right-w
         y=top-h
         print(x,y,x+w,y+h)
         top = int(top * r)
         right = int(right * r)
         bottom = int(bottom * r)
         left = int(left * r)'''
        #cv2.rectangle(rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(rgb, (left, top), (right, bottom), (0, 255, 0), 2)
        crop = rgb[top:bottom, left:right]
        cv2.imwrite("0000"+str(i)+".png", crop)
        i += 1
        # cv2.rectangle(resize, (,h x), (y, w), (255, 0, 0), 2)
        # cv2.rectangle(img,(x,y),(x-30,y-6),(255,255,255),2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = resize[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #	cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0),2)

    cv2.imshow('img', rgb)
    if i >= 50:
        break
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
cap.stop()
