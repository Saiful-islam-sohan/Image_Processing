import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("E:/CSE 4-1/Image Processing/Image/s1.jpeg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



contrast_img = np.zeros_like(gray_img, dtype=np.float64)

r1 = int(input('Enter r1 : '))
r2 = int(input('Enter r2 : '))
s1 = int(input('Enter s1 : '))
s2 = int(input('Enter s2 : '))

a = s1 / r1
b = (s2 - s1) / (r2 - r1)
c = (255 - s2) / (255 - r2)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):

        if gray_img[i][j] < r1:
            contrast_img[i][j] = a * contrast_img[i][j]
        elif gray_img[i][j] < r2:
            contrast_img[i][j] = b * (gray_img[i][j] - r1) + s1
        else:
            contrast_img[i][j] = c * (gray_img[i][j] - r2) + s2


contrast_img = np.clip(contrast_img, 0, 255).astype(np.uint8)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('Original Grayscale Image')
plt.subplot(1, 2, 2)
plt.imshow(contrast_img, cmap='gray')
plt.title('Contrast Image')

plt.show()