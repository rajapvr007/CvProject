import cv2
import numpy as np
def LOG(image):
    blurred = cv2.GaussianBlur (image, (3, 3), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    edges = cv2.Laplacian (gray, -1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    edges = cv2.threshold (edges, 10,255, cv2.THRESH_BINARY)[1]
    edges=~edges
    return edges
img = cv2.imread('rudra.jpg')

edge=LOG(img)
edge= cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)  
final=cv2.addWeighted (img, 0.8, edge, 0.2,0)
cv2.imshow("img", img)
cv2.imshow("edge", edge)
cv2.imshow("cartoonised", final)
cv2.waitKey(0)
cv2.destroyAllWindows()