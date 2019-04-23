# change to new size
from PIL import Image
import os
# import sys

# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio

def imgResize(imgPath, newSize, save=True):
	img = Image.open(imgPath)
	img = img.resize(newSize, Image.ANTIALIAS)
	if save:
		img.save(os.path.join("batch", imgPath))
	else:
		return img

if __name__ == "__main__":
	print("resizing")
	# for i in range(1, 7):
	# 	imgResize("die{}.png".format(i))
	if not os.path.exists("batch"):
		os.mkdir("batch")
	imgResize("test.png", (66, 50))

	