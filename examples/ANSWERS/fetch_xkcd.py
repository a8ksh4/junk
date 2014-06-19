#!/usr/bin/env python

import sys
import os
from urllib2 import urlopen, HTTPError

url = 'http://imgs.xkcd.com/comics/python.png'
saved_pdf_file = 'xkcd.png'
default_viewer = 'eog'

try:
    URL = urlopen(url)
except HTTPError as e:
    print "Unable to open URL:",e
    sys.exit(1)

pdf_contents = URL.read()
URL.close()

with open(saved_pdf_file,'wb') as XKCD:
    XKCD.write(pdf_contents)

if sys.platform == 'win32':
    cmd = saved_pdf_file
elif sys.platform == 'darwin':
    cmd = 'open ' + saved_pdf_file
else:
    cmd = default_viewer + ' ' + saved_pdf_file

os.system(cmd)