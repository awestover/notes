import os
import sys

BASE = os.path.join(os.environ.get("BASE"), "forfun/notes/latexDocs/base.svg")

def buff(x):
  x = str(x)
  return "ink_img"+(3-len(x))*"0"+x+".svg"

if not os.path.exists("images"):
  os.mkdir("images")

biggest = "ink_img000.svg"
for f in os.listdir("images"):
  if "ink_img" in f:
    biggest = max(biggest, f)
i = 0
while i < 999 and buff(i) <= biggest:
  i += 1
if i >= 999:
  raise Exception("ERROR")

os.system(f"cp {BASE} images/{buff(i)}")

if sys.argv[1] == "tex":
  print("\includesvg[width=0.5\linewidth]{images/"+buff(i)+"}")
else:
  short_name = buff(i).replace(".svg", "")
  real_name = buff(i).replace(".svg", ".png")
  print(f"![{short_name}](images/{real_name})")

os.system(f"open images/{buff(i)}")

