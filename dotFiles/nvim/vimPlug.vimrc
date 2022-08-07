call plug#begin()
	Plug 'ap/vim-css-color'
	Plug 'SirVer/ultisnips'
	Plug 'honza/vim-snippets'
	Plug 'itchyny/vim-gitbranch'
  Plug 'Valloric/YouCompleteMe'
	Plug 'airblade/vim-gitgutter'
	Plug 'scrooloose/nerdcommenter'
	Plug 'scrooloose/nerdtree'
  Plug 'mgee/lightline-bufferline'
  Plug 'itchyny/lightline.vim', {'commit': '78c43c1'}
	Plug 'kaisucode/vim-substitution'
	Plug 'danro/rename.vim'
	Plug 'NLKNguyen/papercolor-theme'
	Plug 'tpope/vim-surround'
	Plug 'luochen1990/rainbow'
	Plug 'lervag/vimtex'
	Plug 'JuliaEditorSupport/julia-vim'
  Plug 'junegunn/fzf'
  Plug 'junegunn/fzf.vim'
  Plug 'lfv89/vim-interestingwords'
  Plug 'gabrielelana/vim-markdown'
  Plug 'junegunn/goyo.vim'
  Plug 'junegunn/limelight.vim'
  Plug 'calviken/vim-gdscript3'
	Plug 'pangloss/vim-javascript'
  Plug 'vim-scripts/indentpython.vim'
  Plug 'vim-jp/vim-cpp'
call plug#end()
" If you modify stuff run
" PlugInstall, or PlugClean
" to get changes

"-------------Auto-Commands--------------"
"Automatically source the Vimrc file on save.
autocmd! bufwritepost $HOME/.config/nvim/vimPlug.vimrc source $HOME/.config/nvim/init.vim

