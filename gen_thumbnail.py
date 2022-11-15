import os
import random
from PIL import Image

a=random.choice(os.listdir('templates'))
print(a)

img = Image.open(file).show()

print(img)