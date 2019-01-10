import os
import pyautogui as pyg
import time

os.system("open /Applications/Mischief-Free.app")
time.sleep(4)
dims = pyg.size()
pyg.click(dims[0]*1013/1440, dims[1]*651/900)
# print(pyg.size())
# print(pyg.position())
