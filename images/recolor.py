# scramble all colors (assumes there is a small discrete ammount of colors)
from kmeansNd import *
from PIL import Image
import numpy as np
import os

import matplotlib.pyplot as plt
from pdb import set_trace as tr

def getImgMids(imgPath, k, show=False):
	img = Image.open(imgPath)
	img = img.resize((32,32), Image.ANTIALIAS)

	if show:
		plt.imshow(img)
		plt.pause(2)

	img = img.convert("RGB")
	datas = img.getdata()

	pts = np.array(datas)/255
	fitpts = getFit(pts, k, 3)*255
	
	if show:
		print(fitpts)
		plt.cla()
		for fitpt in fitpts:
			plt.scatter(np.random.rand(), np.random.rand(), color=fitpt/255)
		plt.show()
	
	return fitpts

# simplify is whether you want to reduce color scheme or scramble color scheme
def imgRecolor(imgPath, numColors, simplify):
	img = Image.open(imgPath)
	mids = getImgMids(imgPath, numColors)
	mids = mids.astype(int)

	newColors = np.random.rand(numColors, 3)*255
	newColors = newColors.astype(int)

	if simplify:
		newColors = mids

	img=img.convert("RGBA")
	datas=img.getdata()
	newDatas=[]
	
	for item in datas:
		if item[3] < 0.1: # transparent
			newDatas.append((255,255,255,0)) # 0 means transparent
		else: # opaque
			citem = item[0:3]
			nextColor = getMid(citem, mids, numColors)
			# newDatas.append(tuple(mids[nextColor]))
			newDatas.append(tuple(newColors[nextColor]))

	img.putdata(newDatas)
	img.save(os.path.join("batch",imgPath))

if not os.path.exists("batch"):
	os.mkdir("batch")
# imgRecolor("test.png", 4, False)
# getImgMids("test.png", 4, show=True)
COLORS = 6
for file in os.listdir():
	if ".png" in file:
		print("recoloring "+ file)
		imgRecolor(file, COLORS, False)
