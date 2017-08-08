import cv2
import os
import numpy as np
import matplotlib

# a test to make sure cv2 is working. Also can be used as basis for
# image-based functions

img = cv2.imread("guitar.jpg")
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()