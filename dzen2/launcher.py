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
from pprint import pprint

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Fully customizable Powerline for dzen2.')
    parser.add_argument('align', help = 'Set alignement of content')
    parser.add_argument('--separator', type = int, help = 'Set powerline separator to display', default = 0)
    parser.add_argument('--longitude', type = float, help = 'Set Longitude', default = 23.885942)
    parser.add_argument('--latitude', type = float, help = 'Set Latitute', default = 45.079162)
    parser.add_argument('--timezone', type = int, help = 'Set Timezone', default = 0)
    parser.add_argument('--font', type = str, help = 'Set custom font.', default = 'ProFontIIx Nerd Font Mono')
    parser.add_argument('--fallback-font', type = str, help = 'Set fallback font.', default = 'Noto Sans CJK JP')
    parser.add_argument('--interface', type = str, help = 'Set network interface', default = 'wlo1')

    args = parser.parse_args()

    # pprint(args)

    FONT1 = args.font
    FONT2 = args.fallback_font
    LONGITUDE = args.longitude
    LATITUDE = args.latitude
    TIMEZONE = args.timezone
    NETWORK_INTERFACE = args.interface
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
