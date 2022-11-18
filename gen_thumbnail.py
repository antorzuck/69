import os
import random
from PIL import Image, ImageDraw, ImageFont
import pixabay.core


def create_thumb(text):
    api = pixabay.core("31414343-0a8a8b47952dd2e97e7b90a34")
    search = api.query(text)
    name = random.randint(100000,999999)
    search[0].download(f"templates/{name}.jpg", "largeImage")

    img = Image.open(f'templates/{name}.jpg')
    drew = ImageDraw.Draw(img)
    logo = "https://quotesholy.com/"
    font = ImageFont.truetype("comicbd.ttf", 30)
    drew.text((10,10), logo, font=font, fill=(255,255,255))
    name1 = random.randint(100000,999999)
    img.save(f"thumbnail/{name1}.png")
    return str(name)+'.png'

