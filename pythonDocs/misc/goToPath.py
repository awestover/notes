
import os
with open("/home/alek/Desktop/documentation/.savedpath.txt", "r") as f:
  x = f.read().strip()
os.system("gnome-terminal --working-directory={}".format(x))

