import cv2
import matplotlib.pyplot as mp

img = cv2.imread('img.jpg')
img = cv2.resize(img, (1920,1080))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
mp.xlabel("grey")
mp.ylabel("range")
mp.hist(img.flatten(),256,[0,255])
mp.title("greyscale histogram")
mp.show()
