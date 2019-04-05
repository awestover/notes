# notes
This contains some documentation for things that I have downloaded. 
Including
 * Linux tools
 * programming libraries
 * code snipets
 * python stuff
 * programming services
 * misc

# atom
* highly configurable text editor
* ctrl shift p to access options
* snippets are cool
* you can add your own with ctrl shift p then type add snippets 

# Mac tools
 * double commander: replacement for finder tool, tab to switch between 2 panes, ctrl t for terminal (so nice!) 

# Linux tools

## kevin says 
# xournalpp is a nice tool for editting pdfs

## bash background process
```
python test.py &
```
note: it can still print stuff to stdout

## zoom
get it as a chrome extension and it downloads the thing I think
for viewing someones screen (video conference)

## team-viewer
you can actually manipulate someone elses screen

## zip on linux
recursively zip a directory
```
zip -r foo.zip dir_path
```

## simplenote


## aliases

https://apple.stackexchange.com/questions/25352/list-all-defined-aliases-in-terminal
type alias
alias='alias'
http://www.hostingadvice.com/how-to/set-command-aliases-linuxubuntudebian/
real way involves editing the file and saving it
`nano ~/.bashrc` add an alias to it `source ~./bashrc` to install it

####examples:
```
# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Alek's aliases
alias lh='python3 -m http.server'

alias gitc='git add . && git commit -m'
alias gitp='git push origin master'
alias gitu='git pull origin master'
alias gitr='git remote add origin '

alias killpy='python3 ~/Desktop/documentation/psKILL.py'
alias android_studio='/usr/local/android-studio/bin/studio.sh'
alias andstud='/usr/local/android-studio/bin/studio.sh'
alias pipg='pip list --format=columns | grep '
```

## file sharing
teletype on atom is good

floobits is cross editor
* go to floobits website 
* infinite free tiral for public repos
* sign up with github account 
* download tool (atom: `apm install floobits`)
* conrol+shift+p
* create or join workspace 
* get a nice directory for it



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

credential store

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

## port forwarding / tunelling

ngrok is ok

localhost.run is really nice (no download beyond openssh-server)
 ssh -R 80:localhost:3000 ssh.localhost.run

localtunnel (from npm)
is ok
lt -s nameofthing -p 3000 

none of these require router config stuff

all should be cross platform

ngrok kinda works

but localtunnel is super cool

npm install -g localtunnel
lt --subdomain X --port 3000






# vim:
  * this is an editor
  * good or bad? hard to say

# zsh
  * this is kind of a cool terminal

# remapping caps to escape
  * pretty good for vim

# python stuff

## pypy
  * cool thing
  * you can massively speed up python programs with this

## pip
```
pip list | grep -o ^a.*
```

## version
import struct;print (struct.calcsize("P") * 8)

## binary opperations

bin(8)='0b100'
bin(16)='0b1000'
8&16=0
8|16=24
8^16=24

## plotting
```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=3, ncols=2)

# then access axs[i][j] and say like axs[i][j].scatter(x,y,c='k')
# for multiple plots

```

##.docm files
* get a .docm file
* unzip it (or unzip them all, might need to be smart about where you put them...)
* look in word/documents.xml
* use python beautiful soup to parse
```python
soup.find_all('checkbox')
soup.find_all("text")
```
* to parse the text probably strip all spaces and stuff
* beware of weird characters
* use utf8 encoding when possible

`<w:t>` tags contain info


##.doc files
You will have to use two different command-line tools, depending if you are working with .doc or .docx format.

For .doc use catdoc:

catdoc foo.doc > foo.txt
For .docx use docx2txt:

docx2txt foo.docx
The latter will produce a file called foo.txt in the same directory as the original.

I'm not sure which Linux distribution you are using, but both catdoc and docx2txt are available from the Ubuntu repositories, for example.

## pdf
PyPDF2


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

## kivy
for making phone apps (apps also work on desktop too)
kivy is for cross platform apps

try to make a phone app

install?
https://kivy.org/docs/installation/installation-linux.html


(Android)

buildozer?
https://kivy.org/docs/guide/packaging-android.html

put it on the google play store

run it from kivy launcher

https://www.youtube.com/watch?v=hVuvcvZ8VSA




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

## ev3dev
this software allows you to program ev3 with python!!!!

`ssh robot@ev3dev.local`
password is maker

https://coderwall.com/p/ohk6cg/remote-access-to-ipython-notebooks-via-ssh
https://pypi.python.org/pypi/python-ev3dev/0.2.2.post1

www.ev3dev.org





# javascript stuff

## timer
```
console.time("nob"); console.timeEnd("nob");
```

# graphics
p5 js is pretty good

# speak.js
text to speech 
pretty cool


# webpack
import statements
organize code better

# minify
obsfucate code so console hacking is harder

# R

## downlaod
```
sudo apt-get update
sudo apt-get install r-base
```


# Latex
Compilation tools(?):
`sudo apt-get install texlive-full`  
Editor:
`sudo apt-get install texmaker`  
`texmaker` to launch editor

# java

## jars
java -jar jarfilename. jar

## processing
is a nice java library

you should set up an alias for it:
processing

* go to website 
* install
* unzip
* run the file ./processing in it

(or on windows etc get the app)


# android studio
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

# dots (graph visualization)
sudo apt-get install graphviz


# Programming services 

## heroku
`heroku ps`
list hours left
heroku is nice for hosting stuff

To provision a mongo database:
`heroku addons:create mongolab`


## notifyjs
js notifications
super easy and awesome

download the code from their website

$.notify("Hello world");
 is a simple example



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


## phase diagrams
http://math.rice.edu/~dfield/dfpp.html

also can do them in python

matplotlib
has a thing called
quiver for vectors

takes in 4 args...



## surge
cool STATIC website hosting service
surge


first
sudo apt-get install nodejs
sudo apt-get install npm

sudo apt-get install nodejs-legacy (I think)

npm install --global surge

surge


## touchpad
go to touchpad in settings
turn it off

I also have a keyboard shortcut


# o my zsh
* warp dirrectory is cool "wd help"
