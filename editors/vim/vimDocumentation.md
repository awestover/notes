# Notes
  This is some information about useful features of vim. It isn't really a cheat sheet, but I can just right down anything that I don't want to forget here.

yaw  - yank around word
daw - delete the word that your cursor is in right now
ci( - change inside ( parenthesis )
ci[


Kevin stuff:
haw - highlight around word
raw  - replace around word 

yy    yank line
qa    this is q followed by any key. This allows you to record something. Press q to stop recording, then type @a or whatever the key was to replay it 
ma    this is m followed by any key. This allows you to set a mark point. Then 'a will take you to the mark
ctrl P  super useful
Confirm ('c') and Replace :

:s/foo/bar/gc
Find the occurrence of 'foo', and before replacing it with 'bar' ask for confirmation.
Vim gives you these options :

replace with bar (y/n/a/q/l/^E/^Y)?
y/n - self explanatory
a - replace all occurrences
q - quit
l - replace the current and stop (last)
^E/^Y - ctrl+e and ctrl+y - scroll down and up respectively.


db    delete word back
dw     delete word forward


see 
vimawesome

for lots of plugins if you really want

also has docs, which is probably more useful

ex:
NERD commenter:
leader ci inverts comment state!
