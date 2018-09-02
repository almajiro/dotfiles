#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

RIGHT_HARD_ARROW = '^fn(powerlinesymbols-14)^fn()'
RIGHT_SOFT_ARROW = '^fn(powerlinesymbols-14)^fn()'
LEFT_HARD_ARROW  = '^fn(powerlinesymbols-14)^fn()'
LEFT_SOFT_ARROW  = '^fn(powerlinesymbols-14)^fn()'

def textParser(text, font, fallbackFont):
    encode = not isAscii(text)

    _text = ''

    if encode == True:
        lastFont = font
        for ch in text:
            if isAscii(ch) or (ch >= "\f000" and ch <= "\ffff"):
                if lastFont == font:
                    _text += ch
                else:
                    _text += setFont(font) + ch
                    lastFont = font
            else:
                if lastFont == fallbackFont:
                    _text += ch
                else:
                    _text += setFont(fallbackFont) + ch
                    lastFont = fallbackFont

    else:
        _text += setFont(font)
        _text += text

    return _text

'''
In python3 rename the unicode type to str, the old str type has been replaced by bytes
'''
def isAscii(text):
    if isinstance(text, str):
        try:
            text.encode('ascii')
        except UnicodeEncodeError:
            return False
    else:
        try:
            text.decode('ascii')
        except UnicodeDecodeError:
            return False

    return True

def setFont(font):
    return '^fn(' + font + ')'

def setForeground(color):
    return '^fg(' + color + ')'

def setBackground(color):
    return '^bg(' + color + ')'
