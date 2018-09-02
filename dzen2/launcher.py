#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

from scripts.helper import \
    setForeground, \
    setBackground, \
    textParser, \
    RIGHT_SOFT_ARROW, \
    RIGHT_HARD_ARROW, \
    LEFT_SOFT_ARROW, \
    LEFT_HARD_ARROW

from scripts import mpdDisplay
from scripts import dateDisplay
from scripts import prayerDisplay
from scripts import gmc

FONT1 = 'ProFontIIx Nerd Font Mono'
FONT2 = 'Noto Sans CJK JP'

LONGITUDE = 60.413533 
LATITUDE = 36.131438
TIMEZONE = 9

NETWORK_INTERFACE='wlo1'
DISPLAY_ALIGN = 'right'
OUTPUT = ''

if DISPLAY_ALIGN == 'right':
    ARROW = LEFT_HARD_ARROW
elif DISPLAY_ALIGN == 'left':
    ARROW = RIGHT_HARD_ARROW

toDisplay = [
    {
        'text'       : mpdDisplay.status(),
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
    }
]

for display in toDisplay:
    text = setForeground(display['background'])
    text += ARROW
    text += setBackground(display['background'])
    text += setForeground(display['color'])

    text += ' ' + textParser(display['text'], FONT1, FONT2) + ' '

    OUTPUT += text

print(OUTPUT)
