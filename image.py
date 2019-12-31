from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 100 * 4
height = 100

image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype(r'arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((100 * t + 30, 30), rndChar(), font=font, fill=rndColor2())
image.save('code.jpg', 'jpeg')