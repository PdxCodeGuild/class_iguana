#Lab 16 Image Manipulation.

#Use the colorsys library to increase the saturation, decrease the saturation, and rotate the hue.
# Colorsys represents colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0 - 255.
# You'll have to convert between these two representations.B to Y.

# Y = 0.299*R + 0.587*G + 0.114*B

import colorsys

from PIL import Image
img = Image.open("lenna_(test_image).png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        # r, g, b = int(r *0.299), int(g * 0.587), int(b * 0.114)
        # y = (r + g + b)//3
        #
        # pixels[i, j] = (y, y, y)

        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        h, s, v = h*100, s*0, v*0

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

img.show()



