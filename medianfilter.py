import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('image.jpg')

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Apply Median Filter
    median = cv2.medianBlur(img, 5)

    # Display Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis('off')

    # Display Median Filtered Image
    plt.subplot(1, 2, 2)
    plt.imshow(median)
    plt.title("Median Filter")
    plt.axis('off')

    plt.show()
