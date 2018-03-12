# -*- coding: utf8 -*-

import dfm.commands as commands
import dfm.mappings as mappings
import dfm.filters as filters


__mappings__ = mappings.FSMappings('/',
    mappings.FSMapping('fzf',
        mappings.Link('fzf', '.fzf'),
    ),
    mappings.FSMapping('git',
        mappings.Copy('gitconfig', '.gitconfig'),
        mappings.Copy('gitignore_global', '.gitignore_global'),
    ),
    mappings.FSMapping('python',
        mappings.Copy('pip.conf', '.pip/pip.conf'),
    ),
    mappings.FSMapping('ssh',
        mappings.Copy('authorized_keys', '.ssh/authorized_keys'),
    ),
    mappings.FSMapping('tmux',
        mappings.Link('tmux.conf', '.tmux.conf'),
    ),
    mappings.FSMapping('vim',
        mappings.Link('vimrc', '.vimrc'),
        mappings.Link('vim', '.vim'),
    ),
    mappings.FSMappings('zsh',
        mappings.Link('zshrc', '.zshrc'),
        mappings.Copy('osx_envs', '.configs/osx_envs', filters=[filters.OSXFilter()]),
        mappings.Copy('linux_envs', '.configs/linux_envs', filters=[filters.LinuxFilter()]),
    ),
)

install_ohmyzsh = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'
install_homebrew = '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'

__commands__ = commands.Commands('/',
    commands.Command(install_ohmyzsh, title='Install oh-my-zsh'),
    commands.Command('~/.fzf/install', title='Install fzf'),
)

__commands__.extend([
    commands.Commands('scripts/',
        commands.Command('install-linux.sh', title='Install system utilities'),
        filters=[filters.LinuxFilter()]
    )
])

__commands__.extend([
    commands.Commands('scripts/',
        commands.Command(install_homebrew, title='Install HomeBrew'),
        commands.Command('install-osx.sh', title='Install system utilities'),
        filters=[filters.OSXFilter()]
    )
])

__commands__.extend([
    commands.Command('echo Hello world!'),
])

