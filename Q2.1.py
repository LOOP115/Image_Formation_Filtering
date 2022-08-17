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


# Add white borders
img = np.insert(img, 0, 255, axis=0)
img = np.insert(img, 0, 255, axis=1)
img = np.insert(img, img.shape[0], 255, axis=0)
img = np.insert(img, img.shape[1], 255, axis=1)

img = np.insert(img, 0, 255, axis=0)
img = np.insert(img, 0, 255, axis=1)
img = np.insert(img, img.shape[0], 255, axis=0)
img = np.insert(img, img.shape[1], 255, axis=1)


kernel1 = np.array([[1, -2, 1],
                    [-2, 0, -2],
                    [1, -2, 1]])
output1 = cv2.filter2D(img, -1, kernel1)
cv2.imshow("o1", output1)
print(len(np.argwhere(output1 != 0)))

cv2.waitKey()
cv2.destroyAllWindows()


def count_intersections(image_path):
    # Read image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image so that walls in maze are one pixel wide
    image_height, image_width = image.shape
    new_height = image_height // 2
    new_width = image_width // 2
    maze = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
    plt.subplot(1, 2, 1)
    plt.imshow(maze, cmap='gray')
    plt.title('Resized image')
    plt.axis('off')

    # Use the following the kernel to filter the maze
    # Intersections will be highlighted as white and the rest are black
    kernel = np.array([[1, -2, 1],
                       [-2, 0, -2],
                       [1, -2, 1]])
    intersections = cv2.filter2D(maze, -1, kernel)
    plt.subplot(1, 2, 2)
    plt.imshow(intersections, cmap='gray')
    plt.title('Kernel applied')
    plt.axis('off')
    plt.show()

    return len(np.argwhere(intersections == 255))
