import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define Weighted Average Kernel
kernel = [[1, 2, 1],
          [2, 4, 2],
          [1, 2, 1]]

# Apply Weighted Average Filter
weighted = cv2.filter2D(img, -1, __import__('numpy').array(kernel, dtype='float32') / 16)

# Display Original and Filtered Image
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(weighted)
plt.title("Weighted Average Filter")
plt.axis('off')

plt.show()
