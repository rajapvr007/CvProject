import cv2
import numpy as np

img = cv2.imread('rudra.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

img_canny = cv2.Canny(img,100,200)
img_canny1 = cv2.cvtColor(img_canny, cv2.COLOR_GRAY2BGR)

cv2.imshow("Original Image", img)
cv2.imshow("Canny", img_canny1)

finalCanny= cv2.addWeighted(img,0.8,img_canny1,0.2,0.0)
cv2.imshow("finalCanny",finalCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()