# walk picture
from PIL import Image
import numpy as np
import os

import matplotlib.pyplot as plt
from pdb import set_trace as tr


def randPicture(imgPath, show=False):
	img = Image.open(imgPath)
	w,h=img.size
	img = img.convert("RGBA")
	datas = np.array(img)

	if show:
		plt.imshow(datas)
		plt.pause(2)

	delta = np.random.randint(0,255,size=(h,w,3)).astype("uint8")
	conta = np.zeros((h,w,1)).astype("uint8")
	total = np.concatenate((delta, conta), axis=2)

	datas = ((total+datas)%256).astype("uint8")

	if show:
		plt.imshow(datas)
		plt.pause(2)
	
	print("Saved")
	datas = datas.reshape(w*h, 4)
	datas = datas.tolist()
	datas = [tuple(datasi) for datasi in datas]
	img.putdata(datas)
	img.save(os.path.join("batch",imgPath))


if not os.path.exists("batch"):
	os.mkdir("batch")
for file in os.listdir():
	if ".png" in file:
		print("randifying "+ file)
		randPicture(file, show=False)

"""
tr()
x=np.ones((4,4,1))
y=np.zeros((4,4,1))
xy=np.concatenate((x,y),axis=2)
"""