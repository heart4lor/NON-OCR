from PIL import Image, ImageFont, ImageDraw

image = Image.new('1', (32, 32), 1)
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('/home/syf/PycharmProjects/NON-OCR/ubuntu-mono.ttf', 32)

draw.text((0, 0), 'A', font=font, fill=0)

image.save('A.png', 'png')