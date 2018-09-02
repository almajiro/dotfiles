#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

import mpd

def status(separator = '|'):
    client = mpd.MPDClient(use_unicode=True)
    client.connect('localhost', 6600)

    if client.status()['state'] == 'play':
        songInfo = client.currentsong()
        text = ' ' + ' ' + songInfo['artist'] + ' ' + separator
        text += '  ' + songInfo['album'] + ' ' + separator
        text += '  ' + songInfo['title']

    elif client.status()['state'] == 'pause':
        songInfo = client.currentsong()
        text = ' ' + ' ' + songInfo['artist'] + ' ' + separator        
        text += '  ' + songInfo['album'] + ' ' + separator        
        text += '  ' + songInfo['title']                        
    elif client.status()['state'] == 'stop':
        text = ' MPD is Stop'

    return text
