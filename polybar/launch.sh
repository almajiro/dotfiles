#!/usr/bin/env sh

## Add this to your wm startup file.

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar
polybar -c ~/.config/polybar/main.ini top &
polybar -c ~/.config/polybar/main.ini bottom &
polybar -c ~/.config/polybar/left.ini top &
polybar -c ~/.config/polybar/left.ini bottom &
polybar -c ~/.config/polybar/top.ini top &
polybar -c ~/.config/polybar/top.ini bottom &
