import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('imp.jpg', 0)

def compute_hist(img):
  h, w = img.shape[:2]
  img2 = np.zeros((h+2,w+2),int)
  h2,w2= img2.shape[:2]
  for i in range(h):
      for j in range(w):
       img2[i+1,j+1]=img[i,j]

  for i in range(h2):
      for j in range(w2):
         if  (i!=0 and j!=0 and i!=h2-1 and j!=w-1) :
           img2[i,j] = round(((img2[i-1,j-1] + img2[i-1,j+1] + img2[i+1,j-1] + img2[i+1,j+1] )+ (img2[i,j-1] + img2[i,j+1]+ img2[i-1,j] + img2[i+1,j]) * 2 + img2[i,j] * 4)/16)

  return img2

img = compute_hist(img)

cv2.imshow('image',img)
cv2.waitKey(0)
