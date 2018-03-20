# -*- coding: utf8 -*-

import dfm.mappings as mappings
import dfm.commands as commands

install_command = 'vim -c ":PluginInstall" -c ":q" -c ":q"'
install_ycm = 'python3 install.py'

__mappings__ = mappings.FSMappings('/')

__commands__ = commands.Commands('vim-plugins',
    commands.Command(install_command, desc='Install vim plugins'),
    commands.Command(install_ycm, desc='Install ycm', cwd='bundle/YouCompleteMe'),
)

