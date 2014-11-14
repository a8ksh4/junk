#!/usr/bin/env python

import sys

def main(args):
    if len(args) > 0:
        limit = int(args[0])
    else:
        limit = 100
    pgen = prime_gen(limit)
    for prime in pgen:
        print prime,

def prime_gen(limit):
    flags = [False] * (limit+1)  # initialize flags

    for i in range(2,limit):
        if flags[i]:
            continue
        for j in range(2*i,limit+1,i):
            flags[j] = True
        yield i  # execution stops here until next value is requested by for-in loop


if __name__ == '__main__':
    main(sys.argv[1:])