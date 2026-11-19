import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Mean Filter
mean = cv2.blur(img, (3, 3))

# Display Original and Filtered Image
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(mean)
plt.title("Mean Filtered Image")
plt.axis('off')

plt.show()
