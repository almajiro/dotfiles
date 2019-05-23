#!/usr/bin/env sh

cmd=$(cat <<EOF | rofi -dmenu -p "Which browser do you want to run?: " -format s
Google Chrome
Google Chrome (Incognito Mode)
Firefox
Firefox Developer Edition
EOF)

case "$cmd" in
    "Google Chrome") google-chrome-stable ;;
    "Google Chrome (Incognito Mode)")  google-chrome-stable --incognito ;;
    "Firefox") firefox ;;
    "Firefox Developer Edition") firefox-developer-edition ;;
    *) sh -c "$cmd" || rofi -e "noting to do $cmd" ;;
esac
