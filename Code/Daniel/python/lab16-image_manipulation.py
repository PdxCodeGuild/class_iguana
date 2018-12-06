from PIL import Image
import colorsys

img= Image.open('lenna.png')
width, height = img.size
pixels = img.load()

# This way of conversion is a "true" greyscale (black/white)
# 
# grey_scale = img.convert('L')
# grey_scale.show()



for i in range(width):
    for j in range(height):
        [r, g, b] = pixels[i, j]

        # This conversion has a more "artsy" greyscale with a sort of sepia tone
        # r = int(0.299*r + 0.587*g + 0.114*b)
        # b = int(0.299*r + 0.587*g + 0.114*b)
        # g = int(0.299*r + 0.587*g + 0.114*b)

        # Modifying saturation (s) and hue (h)
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        s += .5 
        h *= 1/3
        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(r*255)
        g = int(r*255)
        b = int(r*255)

        pixels[i, j] = (r, g, b)

img.show()