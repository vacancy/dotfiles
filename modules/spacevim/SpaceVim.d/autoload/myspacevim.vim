function! myspacevim#before() abort
"  let g:spacevim_disabled_plugins = ['vim-startify']

  set ignorecase
  let g:mapleader = ';'

  let NERDTreeShowHidden=1           " 显示隐藏文件
  let NERDTreeAutoDeleteBuffer=1     " 删除文件时自动删除文件对应 buffer
  let NERDTreeHighlightCursorline=1  " 高亮显示光标所在的文件

  let g:tagbar_autofocus=1
  let g:tagbar_compact=1     " tagbar 子窗口中不显示冗余帮助信息
  let g:tagbar_autoshowtag = 1  " 当编辑代码时，在Tagbar自动追踪变量
  let g:tagbar_sort=0           " 不按照字母顺序排序
  let g:tagbar_foldlevel=99     " 默认展开

  " Templates
  let g:templates_directory='$HOME/.SpaceVim.d/templates'
  let g:username='Jiayuan Mao'
  let g:email='maojiayuan@gmail.com'

  " Snippets
  let g:snips_author="Jiayuan Mao"
  let g:snips_email="maojiayuan@gmail.com"
  let g:snips_github="https://github.com/vacancy"

  " UltiSnips
  let g:UltiSnipsExpandTrigger="<c-f>"
  let g:UltiSnipsJumpForwardTrigger="<c-n>"
  let g:UltiSnipsJumpBackwardTrigger="<c-b>"
  let g:UltiSnipsSnippetDirectories=[$HOME.'/.SpaceVim.d/UltiSnips']

  let g:ultisnips_python_style="google"
  let g:ultisnips_python_quoting_style="single"
  let g:ultisnips_python_triple_quoting_style="double"

  let g:pydocstring_doq_path = "doq"
  let g:pydocstring_formatter = "google"

  let g:copilot_filetypes = {
    \ 'xml': v:true,
    \ 'pddl': v:true,
    \ 'pdsketch': v:true,
    \ 'pd3': v:true,
    \ 'cdl': v:true,
    \ 'markdown': v:true,
    \ 'grammar': v:true,
  \ }

  fun! TrimWhitespace()
    let l:save = winsaveview()
    keeppatterns %s/\s\+$//e
    call winrestview(l:save)
  endfun

  augroup TrimWhitespace
    autocmd!
    autocmd BufWritePre * :call TrimWhitespace()
  augroup END

  function! s:agsearch(query, ...)
    let query = empty(a:query) ? '^(?=.)' : a:query
    let args = copy(a:000)
    let command = '-G ".*\.(c|cc|cpp|h|hpp|py|pdsketch)$" -- ' . fzf#shellescape(query)
    " return call('fzf#vim#grep', ['ag --nogroup --column --color '.command, args])
    return call('fzf#vim#ag_raw', insert(args, command, 0))
  endfunction
  command! -bang -nargs=* AgSearch call s:agsearch(<q-args>, fzf#vim#with_preview({'options': '--delimiter : --nth 4..'}), <bang>0)
  " command! -bang -nargs=* AgSearch call s:agsearch(<q-args>,fzf#vim#with_preview(),<bang>0)
endfunction

function! myspacevim#after() abort
  map <C-l> :bp<cr>
  map <C-h> :bn<cr>
  nnoremap <C-g> :call SpaceVim#mapping#gd()<CR>

  augroup fzf_layer
    autocmd!
    autocmd FileType fzf setlocal nonumber norelativenumber
  augroup END
  nnoremap <silent> <C-o> :Files<cr>
  nnoremap <silent> <C-p> :GFiles<cr>
  nnoremap <silent> <C-t> :Tags<cr>
  nnoremap <silent> <C-k> :AgSearch<cr>
  nnoremap <silent> <C-j> :BLines<cr>
  nnoremap <silent> <C-f> :call SpaceVim#lsp#references()<cr>
endfunction

au BufRead,BufNewFile *.cdl set filetype=cdl | setlocal shiftwidth=2 tabstop=2 expandtab

