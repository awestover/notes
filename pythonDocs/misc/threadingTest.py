import threading

def printit():
      print ("Hello, World!")

t=threading.Timer(5, printit)
t.start()

for i in range(0,10):
	print("hey")


