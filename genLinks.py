
import os

data = ""
for f in os.listdir("."):
    data += f"[{f}]({f})\n"

with open("readme.md", "a") as f:
    f.write(data)
print(data)

