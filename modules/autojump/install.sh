#! /bin/bash
#
# install.sh
# Copyright (C) 2019 Jiayuan Mao <maojiayuan@gmail.com>
#
# Distributed under terms of the MIT license.
#

command -v autojump >/dev/null 2>&1 && echo "autojump has been installed." && exit

cd autojump/autojump
./install.py

