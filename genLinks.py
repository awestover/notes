
import os

data = "\n\n# links\n\n"
for f in os.listdir("."):
    data += f"- [{f}]({f})\n"

with open("readme.md", "a") as f:
    f.write(data)
print(data)

