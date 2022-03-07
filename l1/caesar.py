# -*- coding: utf-8 -*-
import string

class Caesar:
    defaults = {
        'alpha': {
            'default': True,
            'alphabet': string.ascii_lowercase
        },
        'numeric': {
            'default': False,
            'alphabet': string.digits
        },
        'polish': {
            'default': False,
            'alphabet': 'żółćęśąźń'
        },
    }

    def __init__(self, key, opts=None):
        self.key = key
        if opts is None:
            opts = {}
        self.alphabet = ''
        for o in self.defaults:
            if (o in opts and opts[o]) or (o not in opts and self.defaults[o]['default']):
                self.alphabet += self.defaults[o]['alphabet']
        self.alphabet = list(set(self.alphabet))
        self.alphabet.sort()

    def encrypt(self, s, key=None):
        if key is None:
            key = self.key
        uppercase_map = map(lambda l: l.isupper(), s)
        print('ALPHABET:', ''.join(self.alphabet))

        encrypted = [
            self.alphabet[(self.alphabet.index(let) + key) % len(self.alphabet)] if let in self.alphabet
            else let
            for let in list(s.lower())
        ]

        return ''.join([
            c[0].upper() if c[1] else c[0]
            for c in zip(encrypted, uppercase_map)
        ])

    def decrypt(self, s, key=None):
        if key is None:
            key = self.key
        return self.encrypt(s, key=-key)
