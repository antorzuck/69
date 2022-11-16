import os
import random
from PIL import Image, ImageDraw, ImageFont




def create_thumb(text):
	random_image = random.choice(os.listdir('templates'))
	img = Image.open(f'templates/{a}')
	drew = ImageDraw.Draw(img)
	font = ImageFont.truetype("comicbd.ttf", 50)
	drew.text((50, 30), text, font=font, fill=(255,0,0))
	name = random.randint(100000,999999)
	img.save(f"thumbnail/{name}.png")
	return name+'.png'


