#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

import datetime
from prayertime import Prayertime, Calendar, Mazhab, Season
from pprint import pprint

def status(longitude, latitude, timezone):
    now = datetime.datetime.now()
    prayerTime = getPrayerTime(longitude, latitude, timezone, now)

    order = ['Fajr', 'Shrouk', 'Zuhr', 'Asr', 'Maghrib', 'Isha']

    for time in order:
        if prayerTime[time] > now.time():
            break

    text = time + ' ' + str(prayerTime[time].hour) + ':' + str(prayerTime[time].minute)

    return text

def getPrayerTime(longitude, latitude, timezone, now):
    pt = Prayertime(longitude, latitude, timezone, now.year, now.month, now.day)
    pt.calculate()

    times = {
        'Fajr'    : parser(pt._fajr),
        'Shrouk'  : parser(pt._shrouk),
        'Zuhr'    : parser(pt._zuhr),
        'Asr'     : parser(pt._asr),
        'Maghrib' : parser(pt._maghrib),
        'Isha'    : parser(pt._isha)
    }

    return times;

def parser(val):
    intvar = int(val)
    hour = intvar

    val -= intvar
    val *= 60
    minute = int(val)
    
    val -= int(val) 
    val *= 60
    sec = int(val)

    return datetime.time(hour, minute, sec)
