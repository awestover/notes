import os

for fname in os.listdir():
  if ".md" in fname:
    os.system(f"pandoc {fname} -s -o {fname.replace('md','pdf')}")



