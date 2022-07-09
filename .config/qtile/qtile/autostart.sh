#!/bin/sh
source ~/.config/common.sh
xrandr --output eDP-1 --off --output DP-1-1 --off --output HDMI-1-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal
arbtt-capture &
picom --config ~/.config/picom/picom.conf &
