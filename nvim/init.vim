"p  _   _        __      ___              _____             __ _       
" | \ | |       \ \    / (_)            / ____|           / _(_)      
" |  \| | ___  __\ \  / / _ _ __ ___   | |     ___  _ __ | |_ _  __ _ 
" | . ` |/ _ \/ _ \ \/ / | | '_ ` _ \  | |    / _ \| '_ \|  _| |/ _` |
" | |\  |  __/ (_) \  /  | | | | | | | | |___| (_) | | | | | | | (_| |
" |_| \_|\___|\___/ \/   |_|_| |_| |_|  \_____\___/|_| |_|_| |_|\__, |
"                                                                __/ |
"                                                               |___/ 

" almajiro's super neovim config

call plug#begin('~/.local/share/nvim/plugged')
    Plug 'tpope/vim-fugitive'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'ncm2/ncm2'
    Plug 'roxma/nvim-yarp'
    Plug 'roxma/vim-hug-neovim-rpc'
    Plug 'phpactor/phpactor', {'for': 'php', 'do': 'composer install'}
    Plug 'phpactor/ncm2-phpactor', {'for': 'php'}
    Plug 'ncm2/ncm2-ultisnips'
"    Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
"    Plug 'kristijanhusak/deoplete-phpactor'
    Plug 'dylanaraps/wal.vim'
    Plug 'mhinz/vim-startify'
    Plug 'StanAngeloff/php.vim'
    Plug 'jwalton512/vim-blade'
    Plug 'scrooloose/nerdtree'
    Plug 'Shougo/denite.nvim'
    Plug 'godlygeek/tabular'
    Plug 'plasticboy/vim-markdown'
"    Plug 'lvht/phpcd.vim', { 'for': 'php', 'do': 'composer install' }
    Plug 'ryanoasis/vim-devicons'
    Plug 'airblade/vim-gitgutter'
    Plug 'junegunn/goyo.vim'
    Plug 'Shougo/neomru.vim'
    Plug 'Shougo/neoyank.vim'
    Plug 'mattn/emmet-vim'
    Plug 'scrooloose/syntastic'
"    Plug 'vim-scripts/PDV--phpDocumentor-for-Vim'
    Plug 'evidens/vim-twig'
    Plug 'SirVer/ultisnips'
    Plug 'phux/vim-snippets'
call plug#end()

autocmd FileType php setlocal omnifunc=phpactor#Complete

let g:UltiSnipsExpandTrigger="<c-j>"
let g:UltiSnipsJumpForwardTrigger="<c-g>"
let g:UltiSnipsJumpBackwardTrigger="<c-t>"
let g:ultisnips_php_scalar_types = 1

let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_idx_mode = 1
let g:airline_theme='papercolor'
nmap gt <Plug>AirlineSelectPrevTab
nmap gT <Plug>AirlineSelectNextTab

set nobackup
set noswapfile
set autoread
set hidden
set showcmd

syntax enable

set number relativenumber 
autocmd ColorScheme * highlight CursorLineNr ctermfg=228
" set cursorline
" set cursorcolumn

set showmatch
set laststatus=2

let php_sql_query=1
set ruler
set list
set expandtab
set smarttab
set shiftround
set tabstop=4
set softtabstop=4
set shiftwidth=4

colorscheme wal
map <C-e> :NERDTreeToggle<CR>

let g:syntastic_mode_map = {'active_filetypes': ['php', 'javascript','coffee', 'scss', 'css'], "passive_filetypes": ["twig"]}
let g:syntastic_error_symbol='✗'
let g:syntastic_warning_symbol='⚠'
let g:syntastic_style_error_symbol = '✗'
let g:syntastic_style_warning_symbol = '⚠'

" autocmd BufEnter * call ncm2#enable_for_buffer()
" set completeopt=noinsert,menuone,noselect
" let g:deoplete#enable_at_startup = 1

augroup ncm2
  au!
  autocmd BufEnter * call ncm2#enable_for_buffer()
  au User Ncm2PopupOpen set completeopt=noinsert,menuone,noselect
  au User Ncm2PopupClose set completeopt=menuone
augroup END
" inoremap <silent> <expr> <CR> (pumvisible() ? ncm2_ultisnips#expand_or("\<CR>", 'n') : "\<CR>")

let g:phpactorPhpBin = 'php'
let g:phpactorBranch = 'master'
let g:phpactorOmniAutoClassImport = v:true

function! DefinitionJumpPhpactor()
    split
    call phpactor#GotoDefinition()
endfunction

" php code jump
nmap <silent>cj :<C-u>call DefinitionJumpPhpactor()<CR>

" Syntastic config
" set statusline+=%#warningmsg#
" set statusline+=%{SyntasticStatuslineFlag()}
" set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" window split 
nnoremap <silent> <s-j> :split<CR>
nnoremap <silent> <s-l> :vsplit<CR>
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk

nmap <C-s> [denite]
nnoremap [denite] <Nop>

" denite config
call denite#custom#var('file/rec', 'command', ['ag', '--follow', '--nocolor', '--nogroup', '-g', ''])
call denite#custom#var('file/rec', 'matchers', ['matcher_fuzzy', 'matcher_ignore_globs'])
call denite#custom#filter('matcher_ignore_globs', 'ignore_globs',
      \ ['.git/', '__pycache__/', '*.o', '*.make', '*.min.*', 'storage/framework/'])
nnoremap <silent> [denite]s :Denite file/rec<CR>
nnoremap <silent> [denite]b :Denite buffer<CR>
nnoremap <silent> [denite]r :Denite register<CR>
nnoremap <silent> [denite]m :Denite file_mru<CR>
nnoremap <silent> [denite]v :Denite bookmark<CR>
nnoremap <silent> [denite]y :Denite neoyank<CR>
nnoremap <silent> [denite]a :DeniteBookmarkAdd<CR>

" indent
vnoremap > >gv
vnoremap < <gv

" autocmd BufRead,BufNewFile *.twig set filetype=htmljinja<Paste>
"augroup filetypedetect
"    au BufRead,BufNewFile *.twig set filetype=htmljinja
    " au BufRead,BufNewFile *.twig set filetype=twig syntax=htmljinja
"augroup END

autocmd FileType htmldjango.twig inoremap {% {%  %}<Left><Left><Left>
autocmd FileType htmldjango.twig inoremap {{ {{  }}<Left><Left><Left>

autocmd FileType blade inoremap {{ {{  }}<Left><Left><Left>

autocmd FileType php inoremap { {}<Left>
autocmd FileType * inoremap '' ''<Left>
autocmd FileType * inoremap "" ""<Left>
autocmd FileType * inoremap [ []<Left>
autocmd FileType * inoremap ( ()<Left>

" ;s to save in insert mode
inoremap ;s <Esc>:w<CR>

" paste from yank register
nnoremap pp "0p
" open new tab
nnoremap nt :tabnew<CR>
" reload config
nnoremap rr :source ~/.config/nvim/init.vim<CR>
" qq to exit
nnoremap qq :q<CR>
" Press f to focus mode (toggle goyo)
nnoremap f :Goyo<CR>
" no highlight
nnoremap nh :noh<CR>
" easy to PlugInstall
nnoremap pi :PlugInstall<CR>
" Emmet
let g:user_emmet_leader_key='<C-y>'

" PHPDoc Generator
nmap <C-p> [phpdoc]
nnoremap [phpdoc] <Nop>
nnoremap <silent> [phpdoc]g :call PhpDocSingle()<CR>
inoremap [phpdoc]g :call PhpDocSingle()<CR>
let g:pdv_cfg_Type = "mixed"
let g:pdv_cfg_Package = ""
let g:pdv_cfg_Version = "$id$"
let g:pdv_cfg_Author = "almajiro <kuroki@almajiro.net>"
let g:pdv_cfg_Copyright = ""
let g:pdv_cfg_License = ""
let g:pdv_cfg_ReturnVal = "void"

nmap <C-g> [git]
nnoremap [git]s :Gstatus<CR>
nnoremap [git]c :Gcommit<CR>
nnoremap [git]p :Gpush<CR>
