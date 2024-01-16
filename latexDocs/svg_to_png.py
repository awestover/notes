import sys
trigger_file = sys.argv[1]

relevant_images = []
with open(trigger_file, 'r') as f:
    for line in f.readlines():
        if "images/" in line and ".png" in line:
            #  ![ink_img011](images/ink_img011.png)
            start_pos = line.find('(images/') + len("(images/")
            end_pos = line.find('.png)')

            if start_pos == 0 or end_pos == -1:
                continue
            else:
                relevant_images.append(line[start_pos:end_pos])

import os
os.chdir("images")

for fname in relevant_images:
    os.system(f"inkscape {fname}.svg -o {fname}.png")


