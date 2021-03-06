# Path to your oh-my-zsh installation.
export ZSH="/home/steven/.oh-my-zsh"
export ZSH_DISABLE_COMPFIX=true

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git github httpie colored-man-pages command-not-found zsh-syntax-highlighting cargo)

source $ZSH/oh-my-zsh.sh

# Lines configured by zsh-newuser-install
HISTFILE=~/.zsh_history
HISTSIZE=65536
SAVEHIST=65536
setopt sharehistory appendhistory extendedglob
setopt HIST_IGNORE_DUPS         # Don't record an entry that was just recorded again.
setopt HIST_IGNORE_ALL_DUPS     # Delete old recorded entry if new entry is a duplicate.
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/steven/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# If not running interactively, don't do anything
# case $- in
#     *i*) ;;
#       *) return;;
# esac

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# enable color support of ls and also add handy aliases
# if [ -x /usr/bin/dircolors ]; then
#     test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
alias ls='exa --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
# fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

alias l='exa -F'
alias ll='exa -alF --git'
alias la='exa -a'
alias fm='vifm'
lt() {
    if [ -z "$@" ]; then
        exa -lT --git *
    else
        exa -lT --git $@
    fi
}

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e \''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

alias e='nvim'
alias vi='nvim'
#alias dog='highlight -O ansi --force'
# dog() { bat --color=always $@ | less }
alias dog='bat --color=always --pager=never --theme ansi-dark'
alias lynx='lynx -use_mouse'
alias uniq='awk "!v[\$0]++"'
alias py='python3'
alias py3='python3'
alias py2='python2'
alias inplace='inplace -w'
alias git=hub
alias ccze='ccze -mansi'
alias pup='pup -c -p --charset utf8'
alias weather='http --body wttr.in/Champaign\?mQF'
alias gblog='git blog'
alias gt='git tree'
alias zathura='zathura --fork'
alias pacman='pacman --color always'
alias yay='yay --color always'
alias mv="mv -iv"
alias cp="cp -riv"
alias mkdir="mkdir -vp"

export PATH="$PATH:$HOME/go/bin:$HOME/.pub-cache/bin:$HOME/.cargo/bin:$HOME/.local/bin:$HOME/.gem/ruby/2.7.0/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib"

export BROWSER=qutebrowser
export EDITOR=nvim
export VISUAL=nvim

# QMK
export QMK_HOME=/home/steven/gitproj/qmk_firmware

# fzf
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
export FZF_DEFAULT_COMMAND='fd -HI -tf' #'rg --hidden -l ""'
export FZF_CTRL_T_COMMAND='fd -HI -tf' 

if [ "$TERM" = "linux" ]; then
    setfont /usr/share/consolefonts/ter-powerline-v24b.psf.gz
    echo -ne "\e]P01d2021"
    echo -ne "\e]P1d72638"
    echo -ne "\e]P288b92d"
    echo -ne "\e]P3f19d1a"
    echo -ne "\e]P41e8bac"
    echo -ne "\e]P5a21eac"
    echo -ne "\e]P61ba595"
    echo -ne "\e]P7d5d5d5"
    echo -ne "\e]P8565b5e"
    echo -ne "\e]P9d72638"
    echo -ne "\e]Pa88b92d"
    echo -ne "\e]Pbf19d1a"
    echo -ne "\e]Pc1e8bac"
    echo -ne "\e]Pda21eac"
    echo -ne "\e]Pe1ba595"
    echo -ne "\e]Pfe5e5e5"
    clear
fi

if [ -z "$UBUNTU_MENUPROXY" ]; then
  UBUNTU_MENUPROXY=1
fi
bindkey -r '^[/'

# brocode/fw stuff
export FW_CONFIG_DIR="$HOME/.config/fw"
if [[ -x "$(command -v fw)" ]]; then
    if [[ -x "$(command -v fzf)" ]]; then
        eval $(fw print-zsh-setup -f 2>/dev/null)
    else
        eval $(fw print-zsh-setup 2>/dev/null)
    fi
fi

export RTV_EDITOR="nvim '+set ft=markdown' '+norm Go'"

# unsetopt XTRACE
# exec 2>&3 3>&-

# opam configuration
test -r /home/steven/.opam/opam-init/init.zsh && . /home/steven/.opam/opam-init/init.zsh > /dev/null 2> /dev/null || true

XAUTHORITY=$HOME/.Xauthority

PATH="/home/steven/perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="/home/steven/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/home/steven/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/home/steven/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/home/steven/perl5"; export PERL_MM_OPT;

eval "$(starship init zsh)"

# Nix
if [ -e /home/steven/.nix-profile/etc/profile.d/nix.sh ]; then . /home/steven/.nix-profile/etc/profile.d/nix.sh; fi

# ajeetdsouza/zoxide
_zoxide_precmd() {
    zoxide add
}

precmd_functions+=_zoxide_precmd

z() {
    if [ $# -ne 0 ]; then
        _Z_RESULT=$(zoxide query "$@")
        case $_Z_RESULT in
            "query: "*)
                cd "${_Z_RESULT:7}"
                ;;
            *)
                echo "${_Z_RESULT}"
                ;;
        esac
    fi
}

alias zi="z -i"
alias zq="zoxide query"

# NRF52 QMK
export NRFSDK15_ROOT=~/gitproj/nRF5_SDK_15.0.0_a53641a

# jarun/nnn
# key-bookmark pairs
export NNN_BMS="d:$HOME/Desktop;D:$HOME/Downloads;p:$HOME/Pictures;h:$HOME;m:/run/media/$USER;M:$HOME/Music;g:$HOME/gitproj"
export NNN_OPTS="deSH"                                           # binary options to nnn
export NNN_OPENER="$HOME/.config/nnn/plugins/nuke"               # custom opener (see plugin nuke)
export NNN_PLUG='d:dragdrop'           # key-plugin (or cmd) pairs
export NNN_ARCHIVE="\\.(7z|bz2|gz|tar|tgz|zip)$"                 # archives [default: bzip2, (g)zip, tar]
export NNN_COLORS='1234' #(/'#0a1b2c3d'/'#0a1b2c3d;1234')        # context colors [default: '4444' (blue)]
export NNN_FCOLORS='c1e2272e006033f7c6d6abc4'                    # file-specific colors
# export NNN_TRASH=1                                               # use desktop Trash [default: delete]
# export NNN_SEL='/tmp/.sel'                                       # custom selection file
# export NNN_FIFO='/tmp/nnn.fifo'                                  # FIFO to write hovered file path to
# export NNN_LOCKER='saidar -c'                                    # terminal locker
# export NNN_MCLICK='^R'                                           # key emulated by middle mouse click
### NNN_FCOLORS, in order
# Block device              c1
# Char device               e2
# Directory                 27
# Executable                2e
# Regular                   00
# Hard link                 60
# Symbolic link             33
# Missing OR file details   f7
# Orphaned symbolic link    c6
# FIFO                      d6
# Socket                    ab
# Unknown OR 0B regular/exe c4
source "$HOME/gitproj/nnn/misc/quitcd/quitcd.bash_zsh"

# Zephyr
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export ZEPHYR_SDK_INSTALL_DIR=/home/steven/.local/zephyr-sdk-0.11.2

# sharkdp/bat
export BAT_CONFIG_PATH=$HOME/.config/bat.conf
