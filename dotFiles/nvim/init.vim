set linebreak

" --- stuff for writing text documents --- "
set nojoinspaces " makes gq and J work better for combining sentences. (less double spaces).

" ------------Indentation--------------"
set tabstop=2 softtabstop=0 expandtab shiftwidth=2 " Default

au BufRead,BufNewFile *.txt		  setfiletype text
" au BufRead,BufNewFile *.md		setfiletype augmd
" au Syntax augmd runtime! syntax/augmd.vim


set cindent
set cinkeys-=0X^H#
set indentkeys-=0X^H#

augroup configgroup
  autocmd Filetype julia setlocal tabstop=2 softtabstop=0 expandtab shiftwidth=2
  autocmd Filetype py setlocal tabstop=4 softtabstop=0 expandtab shiftwidth=4
  autocmd Filetype c setlocal tabstop=2 softtabstop=0 expandtab shiftwidth=2
  autocmd Filetype cpp setlocal tabstop=2 softtabstop=0 expandtab shiftwidth=2
  autocmd Filetype markdown setlocal tw=65 fo+=t nocindent
  autocmd Filetype text setlocal tw=65 fo+=t nocindent
  autocmd Filetype tex setlocal tw=80
augroup END

" this is to get python to indent with 2/4 spaces
let g:python_recommended_style = 1

" ---------------Style------------"
filetype plugin indent on

syntax on
set cursorline          " highlight current line

fun! TexSpell()
	setlocal spell
	syntax spell toplevel
endfun

" setlocal spell
set spelllang=en_us
inoremap <C-l> <c-g>u<Esc>[s1z=`]a<c-g>u

au BufEnter *.tex inoremap <C-f> <Esc>: silent exec '.!python3 $BASE/forfun/notes/latexDocs/ink.py tex'<CR><CR>:w<CR>
au BufEnter *.md inoremap <C-f> <Esc>: silent exec '.!python3 $BASE/forfun/notes/latexDocs/ink.py md'<CR><CR>:w<CR>
nnoremap <C-f> :exec '!python3 $BASE/forfun/notes/latexDocs/ink_open.py' '"' getline(".") '"'<CR><CR>:w<CR>

"------------Mappings--------------"
let mapleader = ','		"The default leader is '\', but ',' is better.

noremap <leader>q :q<cr>

imap <C-_> <C-o><leader>c<Space>
nmap <C-_> <leader>c<Space>
vmap <C-_> <leader>c<Space>

nnoremap ' `
vnoremap ' `
nnoremap ; :
vnoremap ; :
inoremap jf <esc>
vnoremap jf <esc>
nnoremap xx yydd

vmap <C-B> gq

au BufEnter *.tex nnoremap <leader>l :!pdflatex --shell-escape % > "/dev/null"<CR>
au BufEnter *.tex nnoremap <C-g> :!evince *.pdf &<CR>
" au BufEnter *.md nnoremap <leader>l :!python3 ~/dropbox/forfun/notes/latexDocs/svg_to_png.py<CR>

au BufEnter *.md nnoremap <leader>l :call RunPythonScript(expand('%'))<CR>

function! RunPythonScript(filename)
    let command = '!python3 ~/dropbox/forfun/notes/latexDocs/svg_to_png.py ' . a:filename
    execute command
  endfunction

au BufEnter *.md nnoremap <leader>] :!python3 ~/dropbox/forfun/notes/latexDocs/runpanda.py<CR>
nnoremap <leader>p :call TexSpell()<CR>

nmap <CR> o<ESC>
nmap <space><space> :w<CR>
map <Leader>bg :let &background = ( &background == "dark"? "light" : "dark" )<CR>

inoremap cz <Esc>uI
"Go to normal mode, undo, and go back to insert

nnoremap d "_d
vnoremap d "_d

nnoremap c "_c
vnoremap c "_c

inoremap <C-x> <Esc><S-v>xi
nnoremap <C-x> <S-v>x
vnoremap <C-x> x

"Select all
"If need to copy to clipboard, change to gg"+yG
map <C-a> <Esc>ggVG<CR>
imap <C-a> <Esc>ggVG<CR>

vnoremap <F9> "+yi<Esc>
vnoremap <A-c> "+yi<Esc>

set nonumber			"Activate line numbers.
let g:LineNumbers = 0
nmap <F8> :echom ToggleNums()<CR>
function! ToggleNums()
	let temp = g:LineNumbers
	if temp == 1
		set nonumber
		let g:LineNumbers = 0
	else
		set number
		let g:LineNumbers = 1
	endif
	" execute "set showtabline=".newTabStatus
endfunction

" Highlight all occurences of entire word
nmap haw yaw/<C-r>"<CR>
" nmap <Leader>r :%s//

" Replace all occurences of entire word
nmap raw yaw/<C-r>"<CR>:%s//

au BufEnter *.py imap <F5> <Esc>:w<CR>:!python3 %<CR>
au BufEnter *.py noremap <F5> <Esc>:w<CR>:!python3 %<CR>
au BufEnter *.py imap <Leader>r <Esc>:w<CR>:!python3 %<CR>
au BufEnter *.py noremap <Leader>r <Esc>:w<CR>:!python3 %<CR>


"-------------Color schemes--------------"
" set termguicolors
" let base16colorspace=256
"
" set background=dark

" colorscheme evening
" colorscheme elflord
" colorscheme afterglow

" colorscheme wal
colorscheme PaperColor
" colorscheme late_evening
" colorscheme simpleblack

hi Normal guibg=NONE ctermbg=NONE	
hi LineNr ctermfg=141 ctermbg=NONE
" set background=dark
set background=light

hi clear SpellBad
hi SpellBad ctermfg=Black ctermbg=White

"-------------Split management--------------"
set splitbelow
set splitright

nmap <C-H> <C-W><C-H>
nmap <C-J> <C-W><C-J>
nmap <C-K> <C-W><C-K>
nmap <C-L> <C-W><C-L>

"-------------Search--------------"
set hlsearch
set incsearch
set showmatch
set ignorecase		" Make searching case insensitive
set smartcase		" ... unless the query has capital letters.

"Add highlight removal"
nmap <Leader><space> :nohlsearch<cr>

"-------------Tabs--------------"
" nmap <C-W> :tabclose<cr>
" nmap <C-T> :tabe<cr>

" this completely hides the status bar in vim. I kind of like the clean aeshtetic  
set laststatus=0

set showtabline=1
nmap <C-T> :echom SwapTab()<cr>
function! SwapTab()
	let TabStatus = &showtabline
	let newTabStatus = (TabStatus+1)%3
	execute "set showtabline=".newTabStatus
endfunction
" 0: never
" 1: only if there are at least two tab pages
" 2: always

"-------------Buffers--------------"
" Open new empty tab
nmap <Leader>t :enew<cr>

" Move to the next buffer
nmap <leader>f :bnext<CR>
nmap f<leader> :bnext<CR>

" Move to the previous buffer
nmap <leader>d :bprevious<CR>
nmap d<leader> :bprevious<CR>

" Close the current buffer and move to the previous one
nmap <leader>w :bp <BAR> bd #<CR>
nmap w<leader> :bp <BAR> bd #<CR>

" Be able to switch buffers without saving
set hidden

"-------------Auto-Commands--------------"
"Automatically source the Vimrc file on save.
autocmd! bufwritepost $HOME/.config/nvim/init.vim source %

" an extra lick of style
" au Filetype markdown syn match brobro /\v<(beg|end)/ containedin=ALL
" au Filetype markdown syn match mathy /\v<(lem|prop|cor|thm|pf|rmk|ex|defn|quote|clm)/ containedin=ALL
au Filetype markdown syn match mathy /\v<(TODO)/ containedin=ALL
highlight link brobro Error
highlight link mathy Type

source $HOME/.config/nvim/vimPlug.vimrc
source $HOME/.config/nvim/plugin-config.vimrc

