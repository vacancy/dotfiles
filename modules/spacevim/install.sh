#! /bin/bash
#
# install.sh
# Copyright (C) 2025 Jiayuan Mao <maojiayuan@gmail.com>
#
# Distributed under terms of the MIT license.
#

set -e -x

git clone https://github.com/wsdjeg/SpaceVim ~/.SpaceVim

# Backup existing vim and nvim configurations
# mv ~/.vimrc ~/.vimrc_back
# mv ~/.vim ~/.vim_back
# mv ~/.config/nvim ~/.config/nvim_back

[[ -f ~/.vimrc ]] && mv ~/.vimrc ~/.vimrc_back
[[ -d ~/.vim ]] && mv ~/.vim ~/.vim_back
[[ -d ~/.config/nvim ]] && mv ~/.config/nvim ~/.config/nvim_back

# Install SpaceVim

ln -s ~/.SpaceVim ~/.vim
ln -s ~/.SpaceVim ~/.config/nvim

# If pip exists. Install neovim and python-lsp-server
if command -v pip &> /dev/null
then
  pip install --user neovim python-lsp-server
fi

# If nvm exists, use 22
if command -v nvm &> /dev/null
then
  nvm install 22
  nvm use 22
fi
