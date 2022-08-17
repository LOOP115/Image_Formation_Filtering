import numpy as np
import cv2
from matplotlib import pyplot as plt

maze1 = "images/Asst1_2_maze1.png"
maze2 = "images/Asst1_2_maze2.png"

img = cv2.imread(maze2, cv2.IMREAD_GRAYSCALE)

# Resize
img_height, img_width = img.shape
new_height = img_height // 2
new_width = img_width // 2
# Nearest-neighbor interpolation
img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
cv2.imshow("resize", img)

kernel1 = np.array([[1, -1.1, 1],
                    [-1.1, 0, -1.1],
                    [1, -1.1, 1]])
output1 = cv2.filter2D(img, -1, kernel1)
cv2.imshow("o1", output1)

# output1 = cv2.bitwise_not(output1)
# cv2.imshow("o1", output1)

threshold, output2 = cv2.threshold(output1, 178, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("o2", output2)
print(len(np.argwhere(output2 == 178)) // 2)

cv2.waitKey()
cv2.destroyAllWindows()


def count_deadends(image_path):
    # Read image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image so that walls in maze are one pixel wide
    image_height, image_width = image.shape
    new_height = image_height // 2
    new_width = image_width // 2
    maze = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
    plt.subplot(1, 3, 1)
    plt.imshow(maze, cmap='gray')
    plt.title('Resize image')
    plt.axis('off')

    # Use the following the kernel to filter the maze
    # Dead ends will be composed of 2 pixels with value 0f 178
    # Other pixels of walls will be greater than 178
    kernel = np.array([[1, -1.1, 1],
                       [-1.1, 0, -1.1],
                       [1, -1.1, 1]])
    filtered = cv2.filter2D(maze, -1, kernel)
    plt.subplot(1, 3, 2)
    plt.imshow(filtered, cmap='gray')
    plt.title('Filtering')
    plt.axis('off')

    # All pixels greater than 178 will be converted to zero
    # The rest pixels represent dead ends
    threshold, deadends = cv2.threshold(filtered, 178, 255, cv2.THRESH_TOZERO_INV)
    plt.subplot(1, 3, 3)
    plt.imshow(deadends, cmap='gray')
    plt.title('Threshold')
    plt.axis('off')
    plt.show()

    # Since each dead end is represented by 2 pixels with value of 178, the count need to be divided by 2.
    return len(np.argwhere(deadends == 178)) // 2
