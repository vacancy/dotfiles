# -*- coding: utf8 -*-

import dfm.commands as commands
import dfm.mappings as mappings
import dfm.filters as filters


__mappings__ = mappings.FSMappings('/',
    mappings.FSMappings('fzf',
        mappings.Link('fzf', '.fzf'),
    desc='Config fzf.'),
    mappings.FSMappings('git',
        mappings.Copy('gitconfig', '.gitconfig'),
        mappings.Copy('gitignore_global', '.gitignore_global'),
    desc='Config git.'),
    mappings.FSMappings('python',
        mappings.Copy('pip.conf', '.pip/pip.conf'),
    desc='Config python.'),
    mappings.FSMappings('ssh',
        mappings.Copy('authorized_keys', '.ssh/authorized_keys'),
    desc='Config ssh.'),
    mappings.FSMappings('tmux',
        mappings.Link('tmux.conf', '.tmux.conf'),
    desc='Config tmux.'),
    mappings.FSMappings('vim',
        mappings.Link('vimrc', '.vimrc'),
        mappings.Link('vim', '.vim'),
    desc='Config vim.'),
    mappings.FSMappings('zsh',
        mappings.Link('zshrc', '.zshrc'),
        mappings.Copy('osx_envs', '.configs/osx_envs', filters=[filters.OSXFilter()]),
        mappings.Copy('linux_envs', '.configs/linux_envs', filters=[filters.LinuxFilter()]),
    desc='Config zsh.'),
    mappings.FSMappings('/',
        mappings.Link('../bin', '.bin'),
    desc='Config binary executable.'),
)

install_ohmyzsh = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'
install_homebrew = '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'

__commands__ = commands.Commands('/',
    commands.Command(install_ohmyzsh, desc='Install oh-my-zsh'),
    commands.Command('~/.fzf/install', desc='Install fzf'),

    commands.Commands('scripts/',
        commands.Command('install-linux.sh', desc='Install system utilities'),
        filters=[filters.LinuxFilter()]
    ),

    commands.Commands('scripts/',
        commands.Command(install_homebrew, desc='Install HomeBrew'),
        commands.Command('install-osx.sh', desc='Install system utilities'),
        filters=[filters.OSXFilter()]
    ),

    commands.Command('echo Hello world!'),
)

