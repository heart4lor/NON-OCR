import cv2

img = cv2.imread('in/A.png')
cv2.namedWindow('A')
cv2.imshow('A', img)
cv2.waitKey()
cv2.destroyAllWindows()
