import cv2
img = cv2.imread("img.jpg")
b,g,r = cv2.split(img)
cv2.imwrite('blue.png', b)
cv2.imwrite('gren.png', g)
cv2.imwrite('red.png', r)
