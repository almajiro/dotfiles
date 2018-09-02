#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

from scripts.helper import \
    setForeground, \
    setBackground, \
    setFont, \
    textParser, \
    ARROWS

from scripts import gmc
from scripts import mpdDisplay
from scripts import dateDisplay
from scripts import prayerDisplay
from scripts import interfaceDisplay

import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Fully customizable Powerline for dzen2.')
    parser.add_argument('align', help = 'Set alignement of content')
    parser.add_argument('--separator', type = int, help = 'Set powerline separator to display', default = 0)

    args = parser.parse_args()

    FONT1 = 'ProFontIIx Nerd Font Mono'
    FONT2 = 'Noto Sans CJK JP'

    LONGITUDE = 98.601719 
    LATITUDE = 36.131438

    TIMEZONE = 9

    NETWORK_INTERFACE='wlo1'

    ARROW = ARROWS[args.align][args.separator] 

    toDisplay = [
        {
            'text'       : mpdDisplay.status(ARROWS[args.align][1]),
            'color'      : gmc.color['white'],
            'background' : gmc.color['red400']
        },
        {
            'text'       : prayerDisplay.status(LONGITUDE, LATITUDE, TIMEZONE),
            'color'      : gmc.color['white'],
            'background' : gmc.color['green400']
        },
        {
            'text'       : dateDisplay.date(),
            'color'      : gmc.color['white'],
            'background' : gmc.color['grey400']
        },
        {
            'text'       : interfaceDisplay.ip(NETWORK_INTERFACE),
            'color'      : gmc.color['white'],
            'background' : gmc.color['blue400']
        },
        {
            'text'       : interfaceDisplay.hostname(),
            'color'      : gmc.color['white'],
            'background' : gmc.color['pink700']
        }
    ]

    OUTPUT = ''
    for display in toDisplay:
        if args.align == 'right':
            text = setForeground(display['background'])
            text += setFont(FONT1)
            text += ARROW
            text += setBackground(display['background'])
            text += setForeground(display['color'])
            text += ' ' + textParser(display['text'], FONT1, FONT2) + ' '

            OUTPUT += text
        elif args.align == 'left':
            text = setBackground(display['background'])
            text += setForeground(display['color'])
            text += ' ' + textParser(display['text'], FONT1, FONT2) + ' '
            text += setForeground(display['background'])
            text += setFont(FONT1)
            text += ARROW
            
            OUTPUT += text

    print(OUTPUT)
