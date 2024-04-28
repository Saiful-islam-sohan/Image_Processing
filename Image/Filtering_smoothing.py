import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("E:/CSE 4-1/Image Processing/Image/s1.jpeg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



smooth_img = np.zeros_like(gray_img)
sharp_img =  np.zeros_like(gray_img)

smooth_kernel = np.array([[1, 2, 1],[2, 4, 2], [1, 2, 1]]) / 16

sharp_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, - 1, 0]])

for i in range(1, gray_img.shape[0] - 1):
    for j in range(1, gray_img.shape[1] - 1):
        smooth_img[i][j] = np.sum(gray_img[i - 1 : i + 2, j - 1: j + 2] * smooth_kernel)


for i in range(1, gray_img.shape[0] - 1):
    for j in range(1, gray_img.shape[1] - 1):
        sharp_img[i][j] = np.sum(gray_img[i- 1 : i + 2, j - 1 : j + 2] * sharp_kernel)



smooth_img = np.clip(smooth_img, 0, 255).astype(np.uint8)
sharp_img = np.clip(sharp_img, 0, 255).astype(np.uint8)


plt.figure(figsize=(20, 5))
plt.subplot(1, 3, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(smooth_img, cmap='gray')
plt.title('Smoothing Image')
plt.subplot(1, 3, 3)
plt.imshow(sharp_img, cmap='gray')
plt.title('Sharp Image')
plt.tight_layout()
plt.show()

