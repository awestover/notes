class Animal:
	def __init__(self, name):
		self.name=name

	def getName(self):
		return self.name


class Tiger(Animal):
	def __init__(self, name, num):
		Animal.__init__(self, name)
		self.num = num
	def getNum(self):
		return self.num

animal = Animal("misc")
tiger = Tiger("bob", 2)

print(animal.getName())
print(tiger.getName())
print(tiger.getNum())
