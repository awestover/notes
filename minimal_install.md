# howto do a fresh Ubuntu 18 install

- choose minimal installation when installing (so you don't get crap like thunderbird)

- download Chrome, login

- `sudo apt update`

- vim stuff
  * `sudo add-apt-repository ppa:neovim-ppa/stable`
  * `sudo apt-get update`
  * `sudo apt-get install neovim`
	* swap caps and escape
  * copy over `nvim` config file (to `~/.config/nvim`)
  * `source init.vim`
  * :PlugInstall 
  * making YouCompleteMe work is a bit difficult
    * `sudo apt install build-essential cmake vim python3-dev`
    * run `python3 install.py` in `plugged/YouCompleteMe`
  * fzf: 
    * `git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf`
    * `~/.fzf/install`
  * ag: `sudo apt-get install silversearcher-ag`

- terminal stuff
  * terminal preferences: pure black background, pure white text, hide thing that says file and stuff
  * `sudo apt install curl`
  * `sudo apt install zsh`
  * download oh-my-zsh `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
  * make sure zsh is set as the default terminal `chsh -s $(which zsh)`
  * copy over my `.zshrc` file (note: requires installing a package in ~/.oh-my-zsh/plugins)
    * `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git`


- coding stuff
  * python3 included automatically
  * g++ included automatically
  * `sudo apt install git`
    * `git config --global user.email "you@example.com"`
    * `git config --global user.name "Your Name"`
    * `git config credential.helper store` stores credentials
    * **UPDATE** actually do this with ssh keys
      * ssh-keygen -t rsa -C "your_email@example.com"
      * xclip -sel clip < ~/.ssh/id_rsa.pub
      * add the ssh key to your github account
      * git remote set-url origin git@github.com:username/your-repository.git
  * `sudo apt install nodejs`
  * `sudo apt install npm`

- math stuff
  * LaTeX: 
    * basic install: `sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra`
      * lots of packages: `sudo apt-get install texlive-science`
      * now you can compile with `pdflatex`
    * `latexmk` is useful too, do `sudo apt-get install latexmk`
  * pandoc: `sudo apt-get install -y pandoc`
  * drawing / whiteboard app: xournalpp
    * `sudo add-apt-repository ppa:andreasbutti/xournalpp-master`
    * `sudo apt update`
    * `sudo apt install xournalpp`
    * pdf viewer: `evince` installed by default, seems good

