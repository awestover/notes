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


