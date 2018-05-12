# scramble all colors (assumes there is a small discrete ammount of colors)
from PIL import Image
import os

def imgRecolor(imgPath):
	img = Image.open(imgPath)

	img = img.convert("RGBA")
	datas = img.getdata()

	allColors = set()

	newData = []
	for item in datas:
		allColors.add(item)

	print(allColors)
	# img.putdata(newData)

	# img.save(os.path.join("batch",imgPath))

if not os.path.exists("batch"):
	os.mkdir("batch")
imgRecolor("test.png")

