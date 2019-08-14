
from keras.models import load_model
import pyautogui
import keyboard
import time
import base64
from selenium import webdriver
import numpy as np
from keras.preprocessing import image
import cv2
model = load_model("trex-v8.h5")
driver = webdriver.Chrome()


driver.get("http://www.trex-game.skipser.com/")

canvas = driver.find_element_by_id("gamecanvas")



while True:
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    nparr = np.fromstring(base64.b64decode(canvas_base64), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = img/255
#   img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.blur(img, (3, 3))
    img = img[20:, 70:250+70,0]  #crop important part
    img = cv2.resize(img,(75,50))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    pred = model.predict_classes(img)[0]
    if pred == 0:
        pyautogui.press("space")
    if keyboard.is_pressed("q"):
        break
