import cv2
import numpy as np
def computeKirsch (image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kirsch_masks = np.array([[-3, -3, 5, -3, 0, 5, -3, -3, 5], 
                             [-3, 5, 5, -3, 0, 5, -3, 5, -3], 
                             [5, 5, 5, -3, 0, -3, -3, -3, -3], 
                             [5, 5, -3, 5, 0, -3, -3, -3, -3], 
                             [5, -3, -3, 5, 0, -3, 5, -3, -3], 
                             [-3, -3, -3, 5, 0, -3, 5, 5, -3], 
                             [-3, -3, -3, -3, 0, 5, 5, 5, 5], 
                             [-3, -3, -3, -3, 0, -3, 5, 5, 5]])
    kirsch_edges=np.zeros_like(gray)
    for i in range(8):
        kirsch_edges=np.maximum(kirsch_edges, cv2.filter2D (gray, -1, kirsch_masks[i]))
        edges = cv2.threshold (kirsch_edges, 175, 255, cv2.THRESH_BINARY)[1]
        return edges
img = cv2.imread('rudra.jpg') 
edge=computeKirsch(img)
edge= cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
dst=cv2.addWeighted (img, 0.8, edge, 0.2,0)
cv2.imshow("img", img)
cv2.imshow("edge", edge)
cv2.imshow("cartoonised", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()