from PIL import Image

path = "images/Asst1_1_image.png"
statue_image = Image.open(path)
pixels = statue_image.load()
# Compute the proportion of height of the statue in the image
limit = 3
count = 0
statue_red = []
for i in range(statue_image.width):
    for j in range(statue_image.height):
        if pixels[i, j] == (255, 0, 0):
            statue_red.append(j)
            count += 1
        if count == limit:
            break
statue_ratio = (statue_red[2] - statue_red[0]) / statue_image.height
print(statue_ratio)
