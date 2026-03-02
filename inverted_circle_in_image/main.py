from PIL import Image, ImageDraw
from random import randint
from conditions import circle_condition
from pixel_utils import pixel_invert

IMAGES_DIR = "./images/"

try:
    image = Image.open(IMAGES_DIR+"image.png")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    pixels = image.load()
except FileNotFoundError:
    print("Файл не найден")
    exit()

circle_x = randint(0, width)
circle_y = randint(0, height)
a = min(height, width)
radius = randint(int(a*0.1), int(a*0.9))

for x in range(width):
    for y in range(height):
        if circle_condition(x, y, circle_x, circle_y, radius):
            inverted_pixel = pixel_invert(pixels[x, y])
            draw.point((x, y), inverted_pixel)

try:
    image.save(IMAGES_DIR+"img_inverted.png", "png")
except Exception as e:
    raise e