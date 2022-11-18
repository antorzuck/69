import os
import random
from PIL import Image, ImageDraw, ImageFont




def create_thumb(text):
	random_image = random.choice(os.listdir('templates'))
	img = Image.open(f'templates/{random_image}')
	drew = ImageDraw.Draw(img)
	font = ImageFont.truetype("comicbd.ttf", 100)
	drew.text((150,1100), text, font=font, fill=(255,255,255))
	name = random.randint(100000,999999)
	img.save(f"thumbnail/{name}.png")
	return str(name)+'.png'

