# Modes
* Normal
  h move one character left
  j move one row down
  k move one row up
  l move one character right
  4j move 4 rows down
  6k move 6 rows up 
  w move to beginning of next word
  b move to previous beginning of word
  e move to end of word
  W move to beginning of next word after a whitespace
  B move to beginning of previous word before a whitespace
  E move to end of word before a whitespace
  0 move to the beginning of the line
  $ move to the end of the line
  r change single character
  x delete single character
  yy yank link
  dd delete line -- with my vimrc this does not copy the line
  xx delete and copy line
  p paste from vim 
  u undo
  Ctrl+r redo

  f go to next occurence 
  t go right before next occurence
  Using the ( and ) keys are an alternative way to navigate entire sentences.

  J joins lines
  you can move up and down one displayed line by using gj and gk. That way, you can treat your one wrapped line as multiple lines.

* Insert
i for ’insert’, this immediately switches vim to insert mode
a for ’append’, this moves the cursor after the current character and enters insert mode
o inserts a new line below the current line and enters insert mode on the new line
I moves the cursor to the beginning of the line and enters insert mode
A moves the cursor to the end of the line and enters insert mode
O inserts a new line above the current one and enters insert mode on the new line


* Visual
  v to enter visual mode
  V to enter visual line mode
  <C-V> (Ctrl+V) to enter visual block mode

* Command
  press :
  :%s/foo/bar/g Find and replace

* Replace
  shift+R

  replace text


