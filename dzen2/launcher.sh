#!/usr/bin/env bash

###################################################
# launcher script
# kick this file when user logged in
###################################################


generated_output() {
  while true; do
    ./launcher.py right --separator 4
    sleep 1
  done
}

parameters=" -ta r"
parameters+=" -title-name dzentop"

generated_output | dzen2 $parameters &
