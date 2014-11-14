#!/usr/bin/env python

import urllib2

u = urllib2.urlopen("http://www.google.com")
print  u.info()
print
for line in u:
    print line
