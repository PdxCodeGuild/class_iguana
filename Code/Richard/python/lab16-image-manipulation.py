"""
author: Richard Sherman
2018-12-07
lab16-image-manipulation.py, changes certain aspects of an image using the pillow and colorsys libraries
"""


from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here
        (r, g, b) =  0.299*r + 0.587*g + 0.114*b
        pixels[i, j] = (r, g, b)

img.show()