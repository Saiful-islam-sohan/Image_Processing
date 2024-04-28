import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read the image
img = cv2.imread("E:/CSE 4-1/Image Processing/Image/s1.jpeg")

sum = 0
h, w, _ = img.shape
m = min(h, w)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

diagonal_img = np.zeros((m, m), dtype=np.uint8)

for i in range(diagonal_img.shape[0]):
    for j in range(diagonal_img.shape[1]):
        if i == j:
            sum += gray_img[i][j]
            diagonal_img[i][j] = 0
        else:

            diagonal_img[i][j] = gray_img[i][j]

print("total sum of the diagonal value is : ", sum)
plt.imshow(diagonal_img, cmap='gray')
plt.title('After Add Diagonal Value')

plt.show()