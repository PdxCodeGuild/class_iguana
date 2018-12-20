import colorsys
import os

from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

for i in range(1000):
    x0 = randint(0, width)
    y0 = randint(0, height)
    x1 = randint(0, width)
    y1 = randint(0, height)
    line_width = randint(1, 40)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

img.show()

# os.system('pwd')
# from PIL import Image
# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()
# for i in range(width):
#     for j in range(height):
#         r, g, b, = pixels[i, j]
#         # colorsys uses colors in the range [0, 1]
#         h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
#
#         # do some math on h, s, v
#         h *= 45
#         s *= 30
#
#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
#
#         # convert back to [0, 255]
#
#         r = int(r * 255)
#         g = int(g * 255)
#         b = int(b * 255)
#
#         # your code here
#         Y = int(0.299 * r), int(0.587 * g), int(0.114 * b)
#         pixels[i, j] = (r, g, b)
#
#
#
#
# img.show()