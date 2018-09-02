#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

import socket
import netifaces

def ip(interface):
    ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
    return ip

def hostname():
    hostname = socket.gethostname()
    return hostname

