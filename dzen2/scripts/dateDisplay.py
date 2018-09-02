#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

import datetime

def date():
    now = datetime.datetime.now()
    text = ' ' + str(now.year) + "/" + str(now.month).zfill(2) + "/" + str(now.day).zfill(2)

    return text

