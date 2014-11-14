#!/usr/bin/env python

import sys
import os
from datetime import datetime

if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    print "Syntax: {0} directory".format(sys.argv[0])
    sys.exit(1)

# get files in specified directory and prepend the full path

fileinfo = []
filenames = os.listdir(directory)
for filename in filenames:
    full_path = os.path.join(directory,filename)
    if os.path.isfile(full_path):
        fileinfo.append((filename,os.path.getmtime(full_path)))

# fileinfo looks like:
# [(filename, timestamp), (filename, timestamp), ...]

# sort files by timestamp
sorted_fileinfo = sorted(fileinfo,key=lambda e: e[1])

# copy name and timestamp from tuple
name, timestamp = sorted_fileinfo[0]

# convert from Unix timestamp to python datetime object
filedate = datetime.fromtimestamp(timestamp)

# print as human-readable date (which it defaults to)
print name, filedate
