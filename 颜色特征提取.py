from PIL import Image, ImageColor, ImageEnhance, ImageDraw

image = Image.open("1.jpg")
image.show()
image.copy().convert('L').show()
image.copy().convert('HSV').show()

