class Animal:
  def __init__(self, color="green"):
    self.color = color
    if type(color) != str:
      raise ValueError
    if color == "brown":
      raise Exception("thats gross")

  def getColor(self):
    return "imma "+self.color+str(type(self))


class Cat(Animal):
  def __init__(self, color="red", furtype="soft"):
    super().__init__(color)
    self.furtype = furtype
  def brushHair(self):
    print(f"awwww my fur is so {self.color} and {self.furtype}")

class Dog(Animal):
  def __init__(self, color="yellow"):
    super().__init__(color)
    self.bark = "loud"
  def die(self):
    self.bark = "soft"

class AngryCat(Cat):
  def __init__(self, color="red"):
    Animal.__init__(self, color)
    assert self.color == "red"

  def brushHair(self):
    print("DONT YOU DARE")


try:
  Dog(123)
except:
  print("thats a werid color you trting over thehre")
try:
  Cat("brown")
except:
  print("thats a werid color you trting over thehre")


animals=[Animal(), Dog(), Cat(), AngryCat()]
for a in animals:
  print(a.getColor())
animals[2].brushHair()
animals[3].brushHair()



