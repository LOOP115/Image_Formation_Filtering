import numpy as np
import cv2

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

kernel1 = np.array([[1, -2, 1],
                    [-2, 0, -2],
                    [1, -2, 1]])
output1 = cv2.filter2D(img, -1, kernel1)
cv2.imshow("o1", output1)
print(len(np.argwhere(output1 != 0)))

# kernel1 = np.array([[0.5, -0.5, 0.5],
#                     [-0.5, 4, -0.5],
#                     [0.5, -0.5, 0.5]])
# output1 = cv2.filter2D(img, -1, kernel1)
# cv2.imshow("o1", output1)

# output1 = cv2.bitwise_not(output1)
# cv2.imshow("o1", output1)

# kernel2 = np.array([[1/12, 2/12, 1/12],
#                     [2/12, 0, 2/12],
#                     [1/12, 2/12, 1/12]])
# output2 = cv2.filter2D(output1, -1, kernel2)
# cv2.imshow("o2", output2)

# output2 = cv2.bitwise_not(output2)
# cv2.imshow("o2", output2)

# threshold, output3 = cv2.threshold(output2, 32, 255, cv2.THRESH_BINARY)
# cv2.imshow("o3", output3)
# print(len(np.argwhere(output2 != 255)))

cv2.waitKey()
cv2.destroyAllWindows()
