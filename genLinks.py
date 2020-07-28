
import os

def generate_links(path):
    print(path)
    data = "\n# links\n\n"
    for f in os.listdir(path):
        data += f"- [{f}]({f})\n"

    try:
        with open(os.path.join(path, "README.md"), "r") as f:
            prior_content = f.read()
    except:
        prior_content = ""

    try:
        clip_idx = prior_content.rindex("# links")
    except: # none found
        clip_idx = -1

    with open(os.path.join(path, "README.md"), "w") as f:
        f.write(prior_content[:clip_idx])
        f.write(data)
    print(prior_content[:clip_idx])
    print(data)
    print("\n"*3)


generate_links(".")
for path in os.listdir("."):
    if os.path.isdir(path):
        generate_links(path)

