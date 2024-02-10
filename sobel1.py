import cv2
import numpy as np

img = cv2.imread('rudra.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely
img_sobel1= cv2.cvtColor(img_sobel, cv2.COLOR_GRAY2BGR)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel", img_sobelx + img_sobely)
finalSobel =  cv2.addWeighted(img,0.9,img_sobel1,0.1,0.0)
cv2.imshow("finalSobel",finalSobel)


cv2.waitKey(0)
cv2.destroyAllWindows()