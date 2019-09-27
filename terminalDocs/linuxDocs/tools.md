# Linux tools

# tmux!!
# vim!!

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

## kill stuff
```
ps
kill -KILL ps number
killall -KILL [process name]
```
you could also just close the current terminal


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

# dots (graph visualization)
sudo apt-get install graphviz


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


## touchpad
go to touchpad in settings
turn it off

I also have a keyboard shortcut

