import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

maze1 = "images/Asst1_2_maze1.png"
maze2 = "images/Asst1_2_maze2.png"

img = cv2.imread(maze2, cv2.IMREAD_GRAYSCALE)
cv2.imshow("original image", img)
kernel1 = np.array([[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]])
output1 = cv2.filter2D(img, -1, kernel1)
cv2.imshow("original image", output1)
