#!/usr/bin/env python

from struct import pack, unpack

values = 7, 6, 42.3, 'Guido'

binary_stream = pack('iif10s', *values)

new_values = unpack('iif10s', binary_stream)

print new_values
