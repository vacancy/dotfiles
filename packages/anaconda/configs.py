# -*- coding: utf8 -*-

import dfm.mappings as mappings
import dfm.commands as commands

install_ycm = 'bash install.sh'

__mappings__ = mappings.FSMappings('/')

__commands__ = commands.Commands('anaconda',
    commands.Command(install_command, desc='Install Anaconda'),
)

