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
for i in range(1, width-1):
    for j in range(1, height-1):

        Fx = 0
        Fy = 0

        a = img.getpixel((i-1, j-1))
        r = a[0]
        g = a[1]
        b = a[2]

        intensity = r + g + b

        Fx += -intensity
        Fy += -intensity

        a = img.getpixel((i-1, j))
        r = a[0]
        g = a[1]
        b = a[2]

        Fx += -2 * (r + g + b)

        a = img.getpixel((i-1, j+1))
        r = a[0]
        g = a[1]
        b = a[2]

        Fx += -(r + g + b)
        Fy += -(r + g + b)



for i in range(width // 2, width):
    for j in range(1, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (0, 155, b))
        #find a function that gives you a number from 0 to 255
        #rand something input to r, g, b

new_img.save(output_path)
