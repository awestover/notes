import numpy as np
import matplotlib.pyplot as plt

def bufferedNextStep(array):
	arr=np.copy(array)
	for i in range(1, len(arr)-1):
		for j in range(1, len(arr[i])-1):
			local_sum=0
			for k in [-1,1]:
				local_sum += array[i+k][j]
				local_sum += array[i][j+k]
			arr[i][j] = (array[i][j]*0 + local_sum) % 4
	return arr

px=128
board=np.zeros((px,px))
board[px//2][px//2]=1

def addRandomPt(array):
	array[np.random.randint(0,len(array))][np.random.randint(0,len(array))] = 1
	return array

for itt in range(100):
	if itt % 2==0:
		print(itt)
	plt.imshow(board)
	plt.pause(0.01)
	board = bufferedNextStep(board)
	if itt % 5==0:
		board = addRandomPt(board)
