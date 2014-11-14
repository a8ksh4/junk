#!/usr/bin/env python

from sh import tr
fruits = 'apple banana mango orange'.split()
print(tr("[:lower:]", "[:upper:]", _in=fruits))
