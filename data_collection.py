import base64
from selenium import webdriver
import random
import time
import cv2
import numpy as np
import keyboard
driver = webdriver.Chrome()
driver.get("http://www.trex-game.skipser.com/")

canvas = driver.find_element_by_id("gamecanvas")


def data_uri_to_cv2_img(img64):
    nparr = np.fromstring(base64.b64decode(img64), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


count = 5

while True:
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    img = data_uri_to_cv2_img(canvas_base64)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = cv2.blur(img2,(3,3))
    img2 = img2[20:,70:]
    rnd = random.randint(0, 1000000)
    if keyboard.is_pressed("up arrow") and count%5==0:
        print("jump",count)
        cv2.imwrite("data\\jump\\{}.jpg".format(rnd), img2)

    if keyboard.is_pressed("v") and count%5==0:
        print("nothing",count)
        cv2.imwrite("data\\nothing\\{}.jpg".format(rnd), img2)

    if keyboard.is_pressed("o"):
        break
    count += 1