import os
os.chdir("images")

for fname in os.listdir():
  if ".svg" in fname:
    newfname = fname.replace(".svg", ".png")
    os.system(f"inkscape {fname} -o {newfname}")


