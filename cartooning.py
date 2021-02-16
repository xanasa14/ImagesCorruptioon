import cv2
import numpy as np


img = cv2.imread("assets/IMG_1393.jpg")
#edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9 , 9)

#CARTOONING
color = cv2.bilateralFilter(img, 9,250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("images", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
wait = True
while wait:
  wait = cv2.waitKey()=='q113' # hit q to exit
