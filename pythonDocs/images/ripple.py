# ripple colors
from PIL import Image
import numpy as np
import os

import matplotlib.pyplot as plt
from pdb import set_trace as tr
from time import sleep
from numpy.random import randint

speed=1

def addBubble(arr):
	ii = randint(len(arr)//10, 9*len(arr)//10)
	jj = randint(len(arr)//10, 9*len(arr)//10)
	rr = len(arr)//70
	for i in range(ii-rr, ii+rr):
		for j in range(jj-rr, jj+rr):
			arr[i][j] = [0,0,0]

def bufferedNextStep(array):
	arr=np.copy(array)
	for i in range(1, len(arr)-1):
		for j in range(1, len(arr[i])-1):
			local_sum=0
			for k in [-1,1]:
				local_sum += array[i+k][j]
				local_sum += array[i][j+k]
			local_sum = speed*local_sum // 4
			arr[i][j] = (array[i][j] + local_sum) % 256
	return arr

def ripplePicture(imgPath):
	px=128
	img = Image.open(imgPath)
	img = img.resize((px,px), Image.ANTIALIAS)
	img = img.convert("RGB")
	datas = np.array(img)


	# for itt in range(0,15):
		# addBubble(datas)
	try:
		for itt in range(0, 100):
			if itt%10==0:
				print(itt)
			plt.imshow(datas)
			plt.pause(0.5)
			datas = bufferedNextStep(datas)
			# nextStep(datas)
			# addBubble(datas)
	finally:
		print("Saved")
		datas = datas.reshape(px*px,3)
		datas = datas.tolist()
		datas = [tuple(datasi) for datasi in datas]
		img.putdata(datas)
		img.save(os.path.join("batch",imgPath))



ripplePicture("mona-lisa.jpg")
# ripplePicture("dot.png")
# ripplePicture("../../coolGames/land-help/pictures/pictures/oldPics/bear1.png")

"""
Extra stuff

if not os.path.exists("batch"):
	os.mkdir("batch")
for file in os.listdir():
	if ".png" in file:
		print("rippling "+ file)
		ripplePicture(file, COLORS, False)

ripplePicture("test.png")

datas = np.array(img.getdata())
datas.resize(px, px, 3)

img = img.convert("L")

img.putdata(newDatas)
img.save(os.path.join("batch",imgPath))

def nextStep(arr):
	for i in range(1, len(arr)-1):
		for j in range(1, len(arr[i])-1):
			local_sum=0
			for ii in [-1,0,1]:
				for jj in [-1,0,1]:
					if ii != 0 or jj!=0:
						local_sum += arr[ii+i][jj+j]
			local_sum = speed*local_sum // 8
			arr[i][j] = (arr[i][j] + local_sum) % 256


"""
