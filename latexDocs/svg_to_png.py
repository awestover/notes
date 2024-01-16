import sys
trigger_file = sys.argv[1]

relevant_images = []

with open(trigger_file, 'r') as f:
    for line in f.readlines():
        if "images/" in line and ".svg" in line:
            ![ink_img011](images/ink_img011.png)
            start_pos = text.find('(images/') + 1
            end_pos = text.find('.png)')

            if start_pos == 0 or end_pos == -1:
                return continue
            else:
                relevant_images.append(line[start_pos:end_pos]+".svg")

import os
os.chdir("images")

#  for fname in os.listdir():
  #  if ".svg" in fname:
for fname in relevant_images:
    newfname = fname.replace(".svg", ".png")
    os.system(f"inkscape {fname} -o {newfname}")


