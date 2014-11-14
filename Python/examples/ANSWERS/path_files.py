#!/usr/bin/env python

import os

path = os.getenv('PATH')
path_dirs = path.split(os.pathsep)
for path_dir in sorted(path_dirs):
    dir_listing = os.listdir(path_dir)
    print "{0}: {1}".format(path_dir,len(dir_listing))
