import cv2

img = cv2.imread("data\\jump\\1411.jpg")
img = img[:,:265]
print(img.shape)

(130, 265, 3)