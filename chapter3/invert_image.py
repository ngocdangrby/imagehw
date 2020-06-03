import cv2
import numpy
#read and split image
img = cv2.imread("img.jpg")
b,g,r = cv2.split(img)

grey = b
cv2.imwrite('grey.png', grey)
grey_invert = numpy.array([[255-pixel for pixel in line] for line in grey])
cv2.imwrite('grey_invert.png', grey_invert)