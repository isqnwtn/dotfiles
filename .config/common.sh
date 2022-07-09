#!/usr/bin/env bash

[ -f "/home/vismay/.ghcup/env" ] && source "/home/vismay/.ghcup/env" # ghcup-env

export PATH=~/.cabal/bin/:$PATH
export PATH=~/.ghcup/bin:$PATH
export PATH=~/.opam/default/bin:$PATH
export PATH=/home/vismay/.local/bin:$PATH
export PATH=/home/vismay/.cargo/bin:$PATH


alias vim="nvim"
alias fanon="sudo isw -b on"
alias fanoff="sudo isw -b off"

# Functions
# this will do a command repeatedly until its succeded
# needed cause my network sucks!!
# for some reason Ctrl+C wont work here, youll prolly have to kill the terminal
doit () {
    for (( ; ; ))
    do
        $@
        if [ $? -eq 0 ] || [ $? -eq 130 ];
        then
            break
        fi
    done
}

