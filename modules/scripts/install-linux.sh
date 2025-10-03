#!/bin/bash
set -e

# If already root
if [[ "$(id -u)" == '0' ]]
then
    set -x
    locale-gen en_US.UTF-8
    apt-get update
    apt-get install git zsh --yes
    apt-get install build-essential cmake --yes
    apt-get install tmux vim neovim htop nload universal-ctags --yes
    apt-get install silversearcher-ag axel feh jq --yes
    apt-get install git-delta --yes

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    nvm install 22

    apt-get install python3-dev --yes
    exit 0
fi

if [[ "$(whereis sudo)" == *'/'* && "$(sudo -nv 2>&1)" != 'Sorry, user'* ]]
then
    set -x

    sudo locale-gen en_US.UTF-8
    sudo apt-get update
    sudo apt-get install git zsh --yes
    sudo apt-get install build-essential cmake --yes
    sudo apt-get install tmux vim neovim htop nload ctags golang --yes
    sudo apt-get install silversearcher-ag axel feh jq --yes
    sudo apt-get install git-delta --yes

    sudo apt-get install python2.7-dev python3-dev --yes
    sudo apt-get install python-setuptools python3-setuptools --yes
else
    echo "You are not a sudoer."
fi
