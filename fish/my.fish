alias v='nvim'
alias walgen='ranger ~/pictures'

alias vcg='nvim ~/.config/nvim/init.vim'
alias vi3='nvim ~/.config/i3/config'

set -x PASSWORD_STORE_DIR ~/projects/password-store
set -x GNUPGHOME ~/.config/gnupg
set -x PATH ~/.local/share/bin $PATH
set -x PATH ~/.config/composer/vendor/bin/ $PATH
set -x PATH ~/.nodebrew/current/bin $PATH
set -x EDITOR nvim

function fish_greeting
    neofetch
end
