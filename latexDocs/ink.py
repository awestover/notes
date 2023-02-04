import os

BASE = "~/Desktop/forfun/notes/latexDocs/base.svg"

def buff(x):
  x = str(x)
  return "ink_img"+(3-len(x))*"0"+x+".svg"

biggest = "ink_img000.svg"
for f in os.listdir():
  if "ink_img" in f:
    biggest = max(biggest, f)
i = 0
while i < 999 and buff(i) <= biggest:
  i += 1
if i >= 999:
  raise Exception("ERROR")

os.system(f"cp {BASE} {buff(i)}")
print("\includesvg[width=0.5\linewidth]{"+buff(i)+"}")
os.system(f"open {buff(i)}")

