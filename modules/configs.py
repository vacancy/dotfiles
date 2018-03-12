# -*- coding: utf8 -*-

import dfm.commands as commands
import dfm.mappings as mappings
import dfm.filters as filters


__mappings__ = mappings.FSMappings('/',
    mappings.FSMappings('zsh',
        mappings.Link('zshrc', '.zshrc'),
        mappings.Copy('osx_envs', '.configs/osx_envs', filters=[filters.OSXFilter()]),
        mappings.Copy('linux_envs', '.configs/linux_envs', filters=[filters.LinuxFilter()]),
    )
)

__commands__ = commands.Commands('/',
    commands.Command('echo Hello world!')
)