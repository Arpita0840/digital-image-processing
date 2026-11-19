import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('image.jpg')

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Apply Gaussian Filter
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)

    # Display Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis('off')

    # Display Gaussian Filtered Image
    plt.subplot(1, 2, 2)
    plt.imshow(gaussian)
    plt.title("Gaussian Filter")
    plt.axis('off')

    plt.show()
