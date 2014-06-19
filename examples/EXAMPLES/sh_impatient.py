#!/usr/bin/env python

import sh
print sh.ls('-l','/tmp')
print '-' * 50

w = sh.who()
print w
print '-' * 50

diskfull = sh.df('-h')
print diskfull
