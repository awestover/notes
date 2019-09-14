
# you should backup your data
My current solution for doing this is rsync
Basically, get an external hard drive (e.g. STORMLIGHT which has 128 GB space)
and then run something like `rsync -a --progress ~/Desktop/math /Volumes/STORMLIGHT/randBackup`
Note: you should run this somewhat frequently, but it shouldn't take too long to run in the future because rsync isn't stupid, it won't copy stuff that wasn't changed.

