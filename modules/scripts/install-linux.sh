#!/bin/bash

set -e -x

sudo locale-gen en_US.UTF-8
sudo apt-get update
sudo apt-get install build-essential cmake -q
sudo apt-get install git tmux zsh vim htop nload ctags nodejs-dev npm golang -q
sudo apt-get install silversearcher-ag axel feh -q
sudo apt-get install python2.7-dev python3.5-dev -q
sudo apt-get install python-setuptools python3-setuptools -q

