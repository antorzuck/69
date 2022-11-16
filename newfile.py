import json
import os

import random

l = json.dumps({
	"img" : random.choice(os.listdir('templates'))
	})
	
	
print(l)