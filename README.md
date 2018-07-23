# notes
This contains some documentation for things that I have downloaded. 
Including
 * Linux tools
 * programming libraries
 * code snipets
 * python stuff
 * programming services
 * misc




# Linux tools

## zip on linux
recursively zip a directory
```
zip -r foo.zip dir_path
```

## kill stuff
```
ps
kill -KILL ps number
killall -KILL [process name]
```
you could also just close the current terminal

## git
```
git remote add origin X
git pull origin master
git add .
git commit -m "message"
git push origin master

git reset - undoes an add
```

## record stuff
`sudo apt-get install byzanz`

https://www.tecmint.com/best-linux-screen-recorders-for-desktop-screen-recording/

`man byzanz`

https://www.tecmint.com/best-linux-screen-recorders-for-desktop-screen-recording/

```
byzanz-record --help

byzanz-record -d -d 100 f
```


## Desktop Dimmer

can help alter desktop brightness easily

http://www.omgubuntu.co.uk/2017/02/open-source-desktop-dimmer-app
https://github.com/sidneys/desktop-dimmer/releases

https://unix.stackexchange.com/questions/159094/how-to-install-a-deb-file-by-dpkg-i-or-by-apt

sudo dpkg -i /path/to/deb/file
sudo apt-get install -f

## Display and Audio
sudo apt install feh, then feh file.png for image display
https://superuser.com/questions/276596/play-mp3-or-wav-file-via-linux-command-line
sudo apt install sox
play file.wav for sound

## multiple desktops
https://www.pcworld.com/article/2894354/dont-forget-one-of-linuxs-best-features-how-to-use-multiple-workspaces.html
go to appearence
click multiple desktops
switch between with control+alt+arrows




# python stuff

## pip
```
pip list | grep -o ^a.*
```

## plotting
```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=3, ncols=2)

# then access axs[i][j] and say like axs[i][j].scatter(x,y,c='k')
# for multiple plots

```

## good libraries
mammoth - docx to txt

textract
apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig
pip install textract

PDF – pdfminer. http://stackoverflow.com/a/20905381/443457
doc – antiword
docx – python-docx
odt – odt2txt

tkinter
pygame
PIL
matplotlib
seaborn
kivy
numpy
scipy
math
time


## django 
is better than flask
heroku can host django

also can be done locally

django is the back end

html is still front end

note you CAN also use a data base service

recomended postgresql
sudo apt install postgresql-client-common

this stuff will get you into the virtual env
sudo pip install pipenv
pipenv install
pipennv shell




# programming libraries

## processing
is a nice java library

you should set up an alias for it:
processing

* go to website 
* install
* unzip
* run the file ./processing in it

(or on windows etc get the app)


## android studio
annoying install from website, but it is for making phone apps
warning this thing is big! (a couple of Gigabytes)

takes a while

on linux you need to setup an alias for running the studio.sh file

mine are

andstud
or
android_studio

the file is
/usr/local/android_studio/bin/studio.sh

also note the sdk is installed at ~ I think

## dots (graph visualization)
sudo apt-get install graphviz


# Programming services 

## heroku
`heroku ps`
list hours left
heroku is nice for hosting stuff


# general oddities

## compizconfig
linux tool 
you can set a cool mouse thing with this tool 
go to show mouse
windows+k to show the swirling fire mouse thing

## creepy eyes
in a terminal type
```
xeyes
```
and creepy eyes show up





