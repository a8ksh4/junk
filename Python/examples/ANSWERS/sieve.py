#!/usr/bin/env python

import sys

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

flags = [True] * limit

for num in xrange(2,limit):
    if flags[num]:
        print num,
        for multiple_of_num in xrange(2*num,limit,num):
            flags[multiple_of_num] = False
