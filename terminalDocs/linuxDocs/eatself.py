import os
_, mydir = os.path.split(os.getcwd())
os.chdir("..")

xx = input(f"rm -r {mydir}. press enter to confirm")
if len(xx) == 0:
    os.system(f"rm -r {mydir}")


