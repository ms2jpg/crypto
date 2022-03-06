# -*- coding: utf-8 -*-
import string


# http://itre.cis.upenn.edu/~myl/languagelog/archives/003049.html

class Provenzano:
    coding = {'a': 4,		'n': 15,
            'b': 5,		'o': 16,
            'c': 6,		'p': 17,
            'd': 7,		'q': 18,
            'e': 8,		'r': 19,
            'f': 9,		's': 20,
            'g': 10,		't': 21,
            'h': 11,		'u': 22,
            'i': 12,		'v': 23,
            'l': 13,		'z': 24,
            'm': 14}
    decoding = {'4': 'a',		'15': 'n',
            '5': 'b',		'16': 'o',
            '6': 'c',		'17': 'p',
            '7': 'd',		'18': 'q',
            '8': 'e',		'19': 'r',
            '9': 'f',		'20': 's',
            '10': 'g',		'21': 't',
            '11': 'h',		'22': 'u',
            '12': 'i',		'23': 'v',
            '13': 'l',		'24': 'z',
            '14': 'm'}
    punctuation = string.punctuation + ' '
    def encrypt(self, s):
        encrypted = ''
        s = s.lower()
        for letter in s:
            if letter in self.punctuation:
                encrypted += letter
            elif letter in self.coding:
                encrypted += str(self.coding[letter])
        return encrypted

    def decrypt(self, s):
        decrypted = ''
        buf = ''
        for letter in s:
            if letter in self.punctuation:
                decrypted += letter
                continue

            buf += letter
            if buf in self.decoding:
                decrypted += self.decoding[buf]
                buf = ''
                continue
            elif len(buf) >= 3:
                decrypted += buf
                buf = ''
                continue
        return decrypted
