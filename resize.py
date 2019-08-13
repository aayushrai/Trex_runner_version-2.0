import cv2
import numpy as np
import os

if not os.path.exists("data_resize\\"):
    os.mkdir("data_resize\\")
    os.mkdir("data_resize\\jump\\")
    os.mkdir("data_resize\\nothing\\")

for folder in os.listdir("data\\"):
    for file in os.listdir("data\\"+folder+"\\"):
        if not os.path.exists("data_resize\\"+folder+"\\"+file):
                print(file)
                img = cv2.imread("data\\"+folder+"\\"+file)
                img = img[:,:280] # half image on axis = 1
                img = cv2.resize(img,(150,50))
                cv2.imwrite("data_resize\\"+folder+"\\"+file,img)



