import random
import sys
import math
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size
img = img.rotate(45, expand=1)

new_img = Image.new("RGB", (width, height), "white")

for i in range(width // 2, width):
    for j in range(1, height):
        new_img.rotate(180)

for i in range(1, width - 1):
    for j in range(1, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (20, 155, b))

for i in range(width // 2, width):
    for j in range(1, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, 26, b))


new_img.save(output_path)
