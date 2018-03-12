#!/bin/bash

set -e -x

sudo locale-gen en_US.UTF-8
sudo apt-get update
sudo apt-get install build-essential cmake
sudo apt-get install git tmux zsh vim htop nload ctags nodejs-dev npm golang
sudo apt-get install silversearcher-ag axel feh
sudo apt-get install python2.7-dev python3.5-dev
sudo apt-get install python-setuptools python3-setuptools

