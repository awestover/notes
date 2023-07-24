"""
ONLY RUN THIS CODE IF YOU TRUST the file names
"""

import os
import sys

DRAWPATH = "/home/alek/Documents/drawings"

try:
    os.system(f"rm -f {DRAWPATH}/*.pdf")
except Exception as err:
    print(err)

for file in os.listdir(DRAWPATH):
    if ".drawio" in file and ".pdf" not in file:
        filepath = os.path.join(DRAWPATH, file)
        os.system(f"drawio --crop -x -o {filepath}.pdf {filepath}")

