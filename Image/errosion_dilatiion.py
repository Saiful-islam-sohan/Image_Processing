import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define dilation function
def dilation(kernel, morph_img):
    img_height, img_width = morph_img.shape
    kernel_height, kernel_width = kernel.shape
    new_img = np.zeros((img_height - kernel_height + 1, img_width - kernel_width + 1))
    for i in range(new_img.shape[0]):
        for j in range(new_img.shape[1]):
            new_img[i, j] = np.min(morph_img[i:i + kernel_height, j:j + kernel_width] * kernel)
    return new_img.astype("uint8")

# Define erosion function
def erosion(kernel, morph_img):
    img_height, img_width = morph_img.shape
    kernel_height, kernel_width = kernel.shape
    new_img = np.zeros((img_height - kernel_height + 1, img_width - kernel_width + 1))
    for i in range(new_img.shape[0]):
        for j in range(new_img.shape[1]):
            new_img[i, j] = np.max(morph_img[i:i + kernel_height, j:j + kernel_width] * kernel)
    return new_img.astype(np.uint8)

# Define the kernel
kernel = np.ones((10, 10))

# Load the image as grayscale
morph_img = cv2.imread("E:/CSE 4-1/Image Processing/Image/s1.jpeg", cv2.IMREAD_GRAYSCALE)

# Display original and processed images
plt.figure(figsize=(20, 13))
plt.subplot(1, 5, 1)
plt.imshow(morph_img, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 5, 2)
plt.imshow(dilation(kernel, morph_img), cmap='gray')
plt.title('After Dilation')
plt.subplot(1, 5, 3)
plt.imshow(erosion(kernel, morph_img), cmap='gray')
plt.title('After Erosion')
plt.subplot(1, 5, 4)
plt.imshow(dilation(kernel, erosion(kernel, morph_img)), cmap='gray')
plt.title('After Opening')
plt.subplot(1, 5, 5)
plt.imshow(erosion(kernel, dilation(kernel, morph_img)), cmap='gray')
plt.title('After Closing')
plt.tight_layout()
plt.show()
