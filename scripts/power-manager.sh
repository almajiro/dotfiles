#!/usr/bin/env sh

cmd=$(cat <<EOF | rofi -dmenu -p "Power Manager: " -format s
Suspend
Hibernate
Hybrid Sleep
Poweroff
Reboot
Halt
Firmware setup
EOF)

case "$cmd" in
    "Suspend") sudo systemctl suspend ;;
    "Hibernate") sudo systemctl hibernate ;;
    "Hybrid Sleep") sudo systemctl hybrid-sleep ;;
    "Poweroff") sudo systemctl poweroff ;;
    "Reboot") sudo systemctl reboot ;;
    "Halt" ) sudo systemctl halt ;;
    "Firmware setup") sudo systemctl reboot --firmware-setup ;;
    *) sh -c "$cmd" || rofi -e "noting to do $cmd" ;;
esac
