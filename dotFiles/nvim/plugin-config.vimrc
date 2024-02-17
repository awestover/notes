
"-------------Plugins--------------"
"rainbow
let g:rainbow_active = 1 "set to 0 if you want to enable it later via :RainbowToggle

"/ https://castel.dev/post/lecture-notes-1/
"Plug 'lervag/vimtex'
let g:tex_flavor='latex'
let g:vimtex_view_method='zathura'
let g:vimtex_quickfix_mode=0
set conceallevel=1
let g:tex_conceal='abdmg'
" Toggle conceallevel with Control+H
function! ToggleConceallevel()
    if &conceallevel
        set conceallevel=0
    else
        set conceallevel=1
    endif
endfunction
nnoremap <silent> <C-H> :call ToggleConceallevel()<CR>
inoremap fh <Esc>$a<Space>
inoremap hf <Esc>$a
nnoremap fh  A<Space>   

"substitution
let g:substitution_fullwordmatch = 0
let g:substitution_global = 1
let g:substitution_confirmation = 1

"/
"/ markdown

let g:markdown_enable_spell_checking = 0
let g:vim_markdown_math = 1
let g:markdown_enable_conceal = 1
let g:vim_markdown_folding_disabled = 1
set conceallevel=2

"/
"/ Julia-Vim
"
let g:latex_to_unicode_tab = 0

"/ vim-tex
let g:Tex_SmartKeyQuote=1

"/
"/ NERDTree
"/
"Key binding for NERDTreeToggle
function! MyNerdToggle()
	if &filetype == 'nerdtree'
		:NERDTreeToggle 
	else
		:NERDTreeFind
	endif
endfunction
nnoremap <Leader><tab> :call MyNerdToggle()<CR>
set encoding=utf8
let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1
let NERDTreeShowHidden = 1		"Show hidden files

"Open a NERDTree automatically when vim starts up if no files were specified
" autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

"Close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

"Close NERDTree if a file is opened
let NERDTreeQuitOnOpen=1

"Ignoring files
let NERDTreeIgnore=['node_modules$[[dir]]', '__pycache__$[[dir]]', '.git$[[dir]]', '.exe', '.pyc', '.class', '.zip', '.netrwhist']

"After a re-source, fix syntax matching issues (concealing brackets):
"if exists('g:loaded_webdevicons')
"	call webdevicons#refresh()
"endif

"/
"/ lightline
"/
set noshowmode								"Remove ---insert--- below status bar

let g:lightline = {
	  \ 'colorscheme': 'Tomorrow',
	  \ 'active': {
	  \   'left': [ [ 'mode', 'paste' ],
	  \             [ 'gitbranch', 'readonly', 'filename', 'modified' ] ]
	  \ },
	  \ 'component_function': {
	  \   'gitbranch': 'gitbranch#name', 
	  \   'filetype': 'MyFiletype', 
	  \   'fileformat': 'NONE', 
	  \   'fileencoding': 'NONE', 
	  \ },
	  \ }
"function! MyFiletype()
"  return winwidth(0) > 70 ? (strlen(&filetype) ? &filetype . ' ' . WebDevIconsGetFileTypeSymbol() : 'no ft') : ''
"endfunction

let g:lightline#bufferline#shorten_path = 0
" let g:lightline#bufferline#show_number  = 1
let g:lightline#bufferline#unnamed      = '[No Name]'
let g:lightline.tabline          = {'left': [['buffers']], 'right': []}
let g:lightline.component_expand = {'buffers': 'lightline#bufferline#buffers'}
let g:lightline.component_type   = {'buffers': 'tabsel'}

nmap <Leader>1 <Plug>lightline#bufferline#go(1)
nmap <Leader>2 <Plug>lightline#bufferline#go(2)
nmap <Leader>3 <Plug>lightline#bufferline#go(3)
nmap <Leader>4 <Plug>lightline#bufferline#go(4)
nmap <Leader>5 <Plug>lightline#bufferline#go(5)
nmap <Leader>6 <Plug>lightline#bufferline#go(6)
nmap <Leader>7 <Plug>lightline#bufferline#go(7)
nmap <Leader>8 <Plug>lightline#bufferline#go(8)
nmap <Leader>9 <Plug>lightline#bufferline#go(9)
nmap <Leader>0 <Plug>lightline#bufferline#go(10)


"/
"/ UltiSnips
"/
let g:UltiSnipsExpandTrigger = '<C-j>'
"let g:UltiSnipsExpandTrigger = '<Enter>'

"/
"/ vim-gitgutter
"/
set updatetime=250

"/
"/ nerdcommenter
"/
let g:NERDSpaceDelims = 1					" Add spaces after comment delimiters by default
let g:NERDCompactSexyComs = 1				" Use compact syntax for prettified multi-line comments
let g:NERDDefaultAlign = 'left'				" Align line-wise comment delimiters flush left instead of following code indentation

"/
"/ ctrlp
"/
" if exists("g:ctrl_user_command")
"     unlet g:ctrlp_user_command
" endif
" set wildignore+=*.exe,*.class,*.zip,node_modules/**
" let g:ctrlp_user_command = ['.git', 'cd %s && git ls-files -co --exclude-standard']		"Ignore files in .gitignore

" This doesnt work if you're using ag
" let g:ctrlp_custom_ignore = 'node_modules\|DS_Store\|git'
" Use .agignore in home instead

" Makes ctrl+p run faster (Will have to clone and vim-plug the ag package first)
" Without the '-g' in the command, only files specified directly and not recursively will show up
" let g:ctrlp_cache_dir = $HOME . '/.cache/ctrlp'
" if executable('ag')
"   let g:ctrlp_user_command = 'ag %s -l --nocolor --hidden --ignore .git -g ""'
" endif
" " Keeps the match window sized with its default min (1) and max (10) heights, but populates the window with more results
" let g:ctrlp_match_window = 'results:100'

nnoremap <C-p> :Files<Cr>


"/ 
"/ fzf
let g:fzf_preview_window = 'right:60%'

"/
"/ YouCompleteMe
"/
" Stop documentation preview after autocomplete
set completeopt-=preview

"-------------Auto-Commands--------------"
"Automatically source the Vimrc file on save.
autocmd! bufwritepost $HOME/.config/nvim/plugin-config.vimrc source $HOME/.config/nvim/init.vim


