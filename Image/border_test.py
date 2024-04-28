import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("E:/CSE 4-1/Image Processing/Image/s1.jpeg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = gray_img.shape

print(height,width)

square_size= min(height,width)

print(square_size)
crop_x = (width - square_size) // 2
crop_y = (height - square_size) // 2

print(crop_x,crop_y)

cropped_img = gray_img[crop_y:crop_y+square_size, crop_x:crop_x+square_size]
print(cropped_img)