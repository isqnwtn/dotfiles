#!/usr/bin/env bash

prompt="> "
for (( ; ; ))
do
    selected=$(rofi -dmenu -p ${prompt})
    words=($selected)
    case "${words[0]}" in
        "arb")
            alacritty -e "arbtt-tui-exe; exec $SHELL"
            break
            ;;
        "quit")
            break
            ;;
        "exit")
            break
            ;;
        *)

            prompt="$(echo $selected | tr ' ' -) "
            ;;
    esac
done
