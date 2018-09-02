#!/usr/bin/python3

__author__     = "Kuroki Almajiro"
__maintainer__ = "kuroki Almajiro"
__email__      = "kuroki@almajiro.net"
__licence__    = "MIT"
__version__    = "1.0"

import unicodedata

ARROWS = {
    'right': [
        '', '', '', '', '', '', '' , '', '', ''
    ],
    'left': [
        '', '', '', '', '', '', '', '', '', '', '', '', '', ''
    ]
}

def textParser(text, font, fallbackFont):
    encode = not isAscii(text)

    _text = ''

    if encode == True:
        lastFont = font
        _text += setFont(font)
        for ch in text:
            # debug
            # print(ch + "=>" + str(isJapanese(ch)))
            if isAscii(ch) or not isJapanese(ch):
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

def isJapanese(text):
    for ch in text:
        try:
            name = unicodedata.name(ch)

            # debug
            # print(name)
            if "CJK UNIFIED" in name \
                    or "IDEOGRAPHIC FULL STOP" in name \
                    or "FULLWIDTH TILDE" in name \
                    or "HYPHEN-MINUS" in name\
                    or "CORNER BRACKET" in name \
                    or "EXCLAMATION MARK" in name \
                    or "WAVE DASH" in name \
                    or "HIRAGANA" in name \
                    or "KATAKANA" in name:
                return True
        except ValueError:
            return False

    return False

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
