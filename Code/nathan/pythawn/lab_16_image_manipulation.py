from PIL import Image

Image = Image.open('fibonacci_beard.jpg') # must be in same folder
width, height = Image.size
pixels = Image.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        r, g, b = int(r), int(g), int(b)

        y = sum([r, g, b])//3

        pixels[i, j] = (y, y, y)

Image.show()

