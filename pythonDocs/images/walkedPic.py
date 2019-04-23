# walk picture
from PIL import Image
import numpy as np
import os

import matplotlib.pyplot as plt
from pdb import set_trace as tr
from time import sleep
from numpy.random import randint

def randomPos(px):
	return [randint(0,px), randint(0,px)]

def moveRandom(pos, px):
	dx=np.random.choice([-1,0,1])
	dy=np.random.choice([-1,0,1])
	return [(pos[0]+dx)%px, (pos[1]+dy)%px]

def changeColor(array, pos):
	array[pos[0]][pos[1]] = (array[pos[0]][pos[1]] + np.array([10,10,20,0])) % 256


def walkPicture(imgPath):
	px=128
	img = Image.open(imgPath)
	img = img.resize((px,px), Image.ANTIALIAS)
	img = img.convert("RGBA")
	datas = np.array(img)

	pos=randomPos(px)

	try:
		for itt in range(0, 100000):
			if itt%1000==0:
				print(itt)
				plt.imshow(datas)
				plt.pause(0.1)
			pos = moveRandom(pos, px)
			changeColor(datas, pos)
	finally:
		print("Saved")
		datas = datas.reshape(px*px,4)
		datas = datas.tolist()
		datas = [tuple(datasi) for datasi in datas]
		img.putdata(datas)
		img.save(os.path.join("batch",imgPath))

# walkPicture("mona-lisa.jpg")
# walkPicture("dot.png")
# walkPicture("../../coolGames/land-help/pictures/pictures/oldPics/bear1.png")
walkPicture("../../coolGames/land-help/pictures/pictures/currentPics/bear1.png")
