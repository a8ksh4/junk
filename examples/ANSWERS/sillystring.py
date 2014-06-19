#!/usr/bin/env python

def _every_other(self):
    return self._string[::2]

def _init(self, s):
    self._string = s

SillyString = type('SillyString', (object,), { '__init__': _init, 'every_other': _every_other })

ss = SillyString('this is a test')

print ss.every_other()

ss2 = SillyString('Dximd8 *i@tz !w7ogrvkb?#');

print ss2.every_other()