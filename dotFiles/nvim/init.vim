set linebreak

" --- stuff for writing text documents --- "
set nojoinspaces " makes gq and J work better for combining sentences. (less double spaces).

" ------------Indentation--------------"
set tabstop=2 softtabstop=0 expandtab shiftwidth=2 " Default

au BufRead,BufNewFile *.txt		  setfiletype text
au BufRead,BufNewFile *.augmd		setfiletype augmd
au Syntax augmd runtime! syntax/augmd.vim

augroup configgroup
  autocmd Filetype julia setlocal tabstop=4 softtabstop=0 expandtab shiftwidth=4
  autocmd Filetype python setlocal tabstop=2 softtabstop=0 expandtab shiftwidth=2
  autocmd Filetype c setlocal tabstop=4 softtabstop=0 expandtab shiftwidth=4
  autocmd Filetype cpp setlocal tabstop=4 softtabstop=0 expandtab shiftwidth=4
  autocmd Filetype markdown setlocal tw=65 fo+=t
  autocmd Filetype text setlocal tw=65 fo+=t
  autocmd Filetype tex setlocal tw=65
augroup END

set cindent
set cinkeys-=0X^H#
set indentkeys-=0X^H#


" ---------------Style------------"
filetype plugin indent on

syntax on
set cursorline          " highlight current line

fun! TexSpell()
	setlocal spell
	syntax spell toplevel
endfun

let g:tex_flavor = 'tex'


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

nnoremap <leader>l :!pdflatex % > "/dev/null"<CR>
nnoremap <leader>p :call TexSpell()<CR>

nmap <CR> o<ESC>
nmap <space><space> :w<CR>
map <Leader>bg :let &background = ( &background == "dark"? "light" : "dark" )<CR>


inoremap cz <Esc>uI
"Go to normal mode, undo, and go back to insert
"
" int x = arr[]

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

set number			"Activate line numbers.
let g:LineNumbers = 1
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
" colorscheme evening
colorscheme elflord
" colorscheme afterglow

set background=dark
" set background=light
" colorscheme PaperColor
" colorscheme late_evening
" colorscheme simpleblack

hi Normal guibg=NONE ctermbg=NONE	
hi LineNr ctermfg=141 ctermbg=NONE

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

set showtabline=2
nmap <C-T> :echom SwapTab()<cr>
function! SwapTab()
	let TabStatus = &showtabline
	let newTabStatus = abs(TabStatus-2)
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

source $HOME/.config/nvim/vimPlug.vimrc
source $HOME/.config/nvim/plugin-config.vimrc

