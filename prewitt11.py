import cv2
import numpy as np

img = cv2.imread('rudra.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
img_prewitt = cv2.cvtColor(img_prewittx + img_prewitty,cv2.COLOR_GRAY2BGR)

cv2.imshow("Original Image", img)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)
finalPrewitt =  cv2.addWeighted(img,0.6,img_prewitt,0.4,0.0)
cv2.imshow("finalPrewitt",finalPrewitt)


cv2.waitKey(0)
cv2.destroyAllWindows()