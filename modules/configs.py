# -*- coding: utf8 -*-

import dfm.commands as commands
import dfm.mappings as mappings
import dfm.filters as filters


__mappings__ = mappings.FSMappings('/',
    mappings.FSMappings('fzf',
        mappings.Link('fzf', '.fzf'),
    desc='Config fzf.'),
    mappings.FSMappings('git',
        mappings.Copy('gitconfig', '.gitconfig', overwrite=False),
        mappings.Link('gitignore_global', '.gitignore_global'),
    desc='Config git.'),
    mappings.FSMappings('python',
        mappings.Copy('pip.conf', '.pip/pip.conf', overwrite=False),
    desc='Config python.'),
    mappings.FSMappings('ssh',
        mappings.Copy('authorized_keys', '.ssh/authorized_keys', overwrite=False),
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
        mappings.Link('osx_envs', '.config/osx_envs', filters=[filters.OSXFilter()]),
        mappings.Link('linux_envs', '.config/linux_envs', filters=[filters.LinuxFilter()]),
        mappings.Copy('local_envs', '.config/local_envs', overwrite=False),
    desc='Config zsh.'),
    mappings.FSMappings('neofetch',
        mappings.Link('neofetch', '.config/neofetch'),
    desc='Config neofetch.'),
    mappings.FSMappings('/',
        mappings.Link('../bin', '.bin'),
    desc='Config binary executable.'),
)

__commands__ = commands.Commands('/',
    commands.Commands('',
        commands.Command('scripts/install-linux.sh', desc='Install system utilities.'),
        filters=[filters.LinuxFilter()]
    ),

    commands.Commands('',
        commands.Command('scripts/install-osx.sh', desc='Install system utilities.'),
        filters=[filters.OSXFilter()]
    ),

    commands.Command('zsh/install.sh', desc='Install oh-my-zsh.'),
    commands.Command('fzf/install.sh', desc='Install fzf.'),
    commands.Command('autojump/install.sh', desc='Install autojump.'),

    commands.Command('echo Hello world!'),
)

