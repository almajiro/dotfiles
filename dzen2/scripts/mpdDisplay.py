#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

import mpd

client = mpd.MPDClient(use_unicode=True)
client.connect('localhost', 6600)

def status():
    if client.status()['state'] == 'play':
        songInfo = client.currentsong()
        text = ' ' + songInfo['artist'] + ' / ' + songInfo['title'] + ' / ' + songInfo['album']

    elif client.status()['state'] == 'paused':
        text = 'Paused'
    elif client.status()['state'] == 'stop':
        text = 'Stop'

    return text
