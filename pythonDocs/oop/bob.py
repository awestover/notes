class Prob():
  def __init__(self):
    self.x = 10
  def cake(self):
    print(self.x*"cake")

class Ez(Prob):
  def __init__(self):
    self.y = 20
    Prob.__init__(self)

class Bro(Ez):
  def __init__(self):
    super().__init__()
    self.z = 30

