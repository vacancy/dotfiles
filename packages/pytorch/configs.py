# -*- coding: utf8 -*-

import dfm.mappings as mappings
import dfm.commands as commands

install_command = 'bash install.sh'

__dependencies__ = ['anaconda']

__mappings__ = mappings.FSMappings('/')

__commands__ = commands.Commands('pytorch',
    commands.Command(install_command, desc='Install PyTorch'),
)

