import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(100,2)

k = 3
mids = np.random.rand(k,2)

def getGroups(mids, data):
	groups = [[] for i in range(0,k)]
	for d in data:
		groups[getMid(d, mids)].append(d)
	return groups

def getNewMids(groups):
	avgs = [np.average(groups[i], 0) for i in range(0, k)]
	return np.array(avgs)

def getMid(pt, mids):
	dists = [np.linalg.norm(pt-mids[i]) for i in range(0,k)]
	minIdx = 0
	for i in range(1, k):
		if dists[i] < dists[minIdx]:
			minIdx = i
	return minIdx

def pltItter():
	plt.cla()
	plt.scatter(data.T[0], data.T[1], c='k')
	plt.scatter(mids.T[0], mids.T[1], c='r')
	plt.pause(1)

def pltItterc(groups, mids):
	plt.cla()
	for gr in range(0, k):
		plt.scatter([g[0] for g in groups[gr]], [g[1] for g in groups[gr]], c='C'+str(gr))
	plt.scatter(mids.T[0], mids.T[1], c='r')
	plt.pause(1)

ITTERS = 100
for i in range(ITTERS):
	groups = getGroups(mids, data)
	mids = getNewMids(groups)
	pltItterc(groups, mids)

