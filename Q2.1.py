import os
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

kernel1 = np.array([[1/26, 3/26, 1/26],
                    [3/26, 10/26, 3/26],
                    [1/26, 3/26, 1/26]])
output1 = cv2.filter2D(img, -1, kernel1)
cv2.imshow("o1", output1)

hold, output2 = cv2.threshold(output1, 70, 255, cv2.THRESH_BINARY)
cv2.imshow("o2", output2)
print(len(np.argwhere(output2 != 255)))

cv2.waitKey()
cv2.destroyAllWindows()
