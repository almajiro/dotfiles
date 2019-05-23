#!/usr/bin/env sh

cmd=$(cat <<EOF | rofi -dmenu -p "Fast Access: " -format s
Commander
Zabbix
Data-Hotel ViDC
Git Softmaker
Almajiro Blog
EOF)

case "$cmd" in
    "Commander") google-chrome-stable --new-window http://cmd.cun.cc;;
    "Zabbix") google-chrome-stable --new-window http://monitor.data-hotel.intranet/zabbix ;;
    "Data-Hotel ViDC") google-chrome-stable --new-window http://vidc.data-hotel.intranet ;;
    "Git Softmaker") google-chrome-stable --new-window http://git.softmaker.intranet ;;
    "Almajiro Blog") google-chrome-stable --new-window http://www.almajiro.tokyo ;;
    *) sh -c "$cmd" || rofi -e "noting to do $cmd" ;;
esac
