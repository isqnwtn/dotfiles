#!/usr/bin/env bash

prompt="> "
for (( ; ; ))
do
    selected=$(rofi -dmenu -p ${prompt})
    words=($selected)
    case "${words[0]}" in
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
