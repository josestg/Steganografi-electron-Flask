import numpy as np
from PIL import Image

im = Image.open("../uploads/min_test.png")
pixels = im.load()

x,y = im.size
# print(x*y)
for i in range(x):
	for j in range(y):
		pixels[i,j] = (255,0,0)
	if(i>x/2):
		break
im.save("../uploads/out.png")

