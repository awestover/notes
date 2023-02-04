import sys
import os

vim_stuff = "".join(sys.argv[1:])

if "ink_img" in vim_stuff:
  start_idx = vim_stuff.index("ink_img")
  final_idx = start_idx + len("ink_img000.svg")
  fname = vim_stuff[start_idx:final_idx]

  os.system(f"open {fname}")


