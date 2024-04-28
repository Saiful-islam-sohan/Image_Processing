

import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("E:/CSE 4-1/Image Processing/Image/s1.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def hist_equi_img(img, Tx):
    height, width = img.shape
    equi_img = np.zeros((height, width), "uint8")

    for i in range(height):
        for j in range(width):
            equi_img[i][j] = Tx[img[i][j]]

    return equi_img

def drawHist(img):
    height, width = img.shape
    hist = np.zeros((256))
    cdfTx = np.zeros((256))

    pre_sum = 0

    for i in range(256):
        hist[i] = np.sum(img == i)
        pre_sum += hist[i]
        cdfTx[i] = pre_sum

    hist = hist / (height * width)
    cdfTx = cdfTx * 255 / (height * width)
    cdfTx = cdfTx.astype("uint8")

    return hist, cdfTx

hist, cdfTx = drawHist(gray_img)
equi_img = hist_equi_img(gray_img, cdfTx)

# Plotting original and equalized images
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Equalized image
plt.subplot(2, 2, 2)
plt.imshow(equi_img, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

# Original histogram
plt.subplot(2, 2, 3)
x = np.arange(256)
plt.bar(x, hist, width=0.5)
plt.title('Original Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Equalized histogram
plt.subplot(2, 2, 4)
hist_equi, _ = drawHist(equi_img)
plt.bar(x, hist_equi, width=0.5)
plt.title('Equalized Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
