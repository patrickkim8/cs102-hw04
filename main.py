import random
import sys
import math
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

# TODO: Replace this with your own filter!
# Median pixel filter, taken from https://note.nkmk.me/en/python-opencv-pillow-image-size

for i in range(1, width - 1):
    for j in range(1, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, 26, b))


for i in range(width // 2, width):
    for j in range(1, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (20, 155, b))
        #find a function that gives you a number from 0 to 255
        #rand something input to r, g, b

new_img.save(output_path)
