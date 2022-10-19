#!/bin/bash

set +e +x

if [[ "$(whereis sudo)" == *'/'* && "$(sudo -nv 2>&1)" != 'Sorry, user'* ]]
then
    sudo locale-gen en_US.UTF-8
    sudo apt-get update
    sudo apt-get install git zsh --yes
    sudo apt-get install build-essential cmake --yes
    sudo apt-get install tmux vim htop nload ctags golang --yes
    sudo apt-get install silversearcher-ag axel feh --yes
    sudo apt-get install python2.7-dev python3-dev --yes
    sudo apt-get install python-setuptools python3-setuptools --yes
else
    echo "You are not a sudoer."
fi
