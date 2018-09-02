#!/usr/bin/env bash

###################################################
# launcher script
# kick this file when user logged in
###################################################

SCRIPT_DIR=$(cd $(dirname $0); pwd)

generated_output() {
  while true; do
    $SCRIPT_DIR/launcher.py right --separator 4 --latitude 36.131438 --longitude 139.601719 --timezone 9 --interface lo
    sleep 1
  done
}

parameters=" -ta r"
parameters+=" -title-name dzentop"

generated_output | dzen2 $parameters &
