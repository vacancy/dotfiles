#=============================================================================
# basic.toml --- basic configuration example for SpaceVim
# Copyright (c) 2016-2022 Wang Shidong & Contributors
# Author: Wang Shidong < wsdjeg@outlook.com >
# URL: https://spacevim.org
# License: GPLv3
#=============================================================================

# All SpaceVim option below [option] section
[options]
    # set spacevim theme. by default colorscheme layer is not loaded,
    # if you want to use more colorscheme, please load the colorscheme
    # layer
    colorscheme = "gruvbox"
    sidebar_width = 40
    colorscheme_bg = "dark"

    # Disable statusline separator, if you want to use other value, please
    # install nerd fonts
    statusline_separator = "nil"
    statusline_iseparator = "bar"
    buffer_index_type = 4
    windows_index_type = 3
    enable_tabline_filetype_icon = false
    enable_statusline_mode = false
    statusline_unicode = false

    # Enable vim compatible mode, avoid changing origin vim key bindings
    bootstrap_before = 'myspacevim#before'
    bootstrap_after = 'myspacevim#after'
    snippet_engine = "ultisnips"

    enable_filetree_gitstatus = true
    filetree_direction = "left"

    relativenumber = false
    enable_cursorline = true
    enable_cursorcolumn = true

[[layers]]
name = "colorscheme"

[[custom_plugins]]
name = "catppuccin/nvim"
flavour = "frappe"

[[custom_plugins]]
name = "NLKNguyen/papercolor-theme"

[[custom_plugins]]
name = "neanias/everforest-nvim"

# Enable autocomplete layer
[[layers]]
name = 'autocomplete'
auto_completion_return_key_behavior = "nil"
auto_completion_tab_key_behavior = "smart"

[[layers]]
name = "ui"
enable_scrollbar = true

[[layers]]
name = "incsearch"

[[layers]]
name = 'git'

[[layers]]
name = 'VersionControl'

[[layers]]
name = 'shell'
default_position = 'float'
default_height = 30

[[layers]]
name = "lang#python"
python_interpreter = "/Users/jiayuanm/miniforge3/envs/summer2024/bin/python"
enable_typeinfo = true

[[layers]]
name = "tools"

[[layers]]
name = 'lsp'
enabled_clients = ['pylsp']

[[custom_plugins]]
repo = "https://github.com/github/copilot.vim"
merged = false

[[custom_plugins]]
repo = "https://github.com/rose-pine/neovim"
merged = false

[[custom_plugins]]
repo = "https://github.com/honza/vim-snippets"
merged = false

[[custom_plugins]]
repo = "https://github.com/aperezdc/vim-template"
merged = false

[[custom_plugins]]
repo = "https://github.com/ludovicchabant/vim-gutentags"
merged = false

[[custom_plugins]]
repo = "https://github.com/junegunn/fzf"
merged = false

[[custom_plugins]]
repo = "https://github.com/junegunn/fzf.vim"
merged = false

