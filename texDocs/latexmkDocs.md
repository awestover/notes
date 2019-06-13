latexmk is an awesome tool
it is included if you installed all of latex

run

latexmk -pvc file.tex -pdf  for UPDATING every time you save!!!

can view as pdf or dvi


dvi notes:

it is cool to view it as a dvi 

the gist of using xdvi is 

xdvi file.dvi

but latexmk takes care of that for you
the thing to watch out for is how to navigate in xdvi

CTRL + / - to zoom in and out ( yeah not command + / - )
q to quit
n for next page
b for previous page
arrows for navigation in page
number g to go to page

note: configs for latexmk are located in ~/.latexmkrc

