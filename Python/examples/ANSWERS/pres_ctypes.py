#!/usr/bin/env python

import sys
import ctypes

# load the library, according to platform
try:
    if sys.platform == 'win32':
        presidents = ctypes.cdll.LoadLibrary(r'..\DATA\presidents.dll')
    elif sys.platform == 'darwin':
        presidents = ctypes.cdll.LoadLibrary('../DATA/presidents.dylib')
    else:
        presidents = ctypes.cdll.LoadLibrary('../DATA/presidents.so.1.0')
except Exception as err:
    print "Unable to load presidents module", err
    exit(1)

presidents.get_name.restype = ctypes.c_char_p

for i in xrange(1,45):
    print presidents.get_name(i)
