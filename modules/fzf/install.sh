#! /bin/bash
#
# install.sh
# Copyright (C) 2019 Jiayuan Mao <maojiayuan@gmail.com>
#
# Distributed under terms of the MIT license.
#

command -v fzf >/dev/null 2>&1 && echo "fzf has been installed." && exit

~/.fzf/install --key-bindings --completion --no-update-rc
