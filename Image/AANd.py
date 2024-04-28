import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read two grayscale images
img1 = cv2.imread("E:/CSE 4-1/Image Processing/Image/s1.jpeg")
img2 = cv2.imread("E:/CSE 4-1/Image Processing/Image/s.png")

# Check if images were loaded successfully
if img1 is None or img2 is None:
    print("Error: One or both images could not be loaded.")
else:
    # Check if image dimensions are valid
    if img1.size == 0 or img2.size == 0:
        print("Error: One or both images have empty dimensions.")
    else:
        # Resize img2 to match the size of img1
        resize_img = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

        # Subtract resized img2 from img1
        res_img = img1 - resize_img

        # Clip and convert the result to the appropriate data type
        res_img = np.clip(res_img, 0, 255).astype("uint8")

        # Display the images
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 3, 1)
        plt.imshow(img1, cmap='gray')
        plt.title('First Image')

        plt.subplot(1, 3, 2)
        plt.imshow(img2, cmap='gray')
        plt.title('Second Image')

        plt.subplot(1, 3, 3)
        plt.imshow(res_img, cmap='gray')
        plt.title('Resultant Image')

        plt.show()
