# converts white to transparent backgruond
from PIL import Image
import os

from os.path import join

def imgTransparent(imgPath, inPlace=True):

	img = Image.open(imgPath)
	img = img.convert("RGBA")
	datas = img.getdata()

	newData = []
	for item in datas:
		if ((255-item[0])+(255-item[1])+(255-item[2])) < 15:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

	img.putdata(newData)

	print("transparent " + imgPath)

	if inPlace:
		img.save(imgPath)
	else:
		img.save(join("batch", imgPath))

## to extract the pngs:
## convert -coalesce blah.gif imgs/%05d.png
## to concatenate the gifs:
## convert -delay 0 -loop 0 -alpha set -dispose previous *.png ani.gif

for i in range(5): 
    imgTransparent(f"{i}.png", inPlace=True)

