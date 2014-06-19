#!/usr/bin/env python

import os

def main():
    os.system("who")

    ls = os.popen("ls -l /tmp","r")

    for entry in ls:
        print entry[:-1]
    print

    # backticks equivalent
    h = os.popen("uname -n").read()[:-1]

    print h

if __name__ == '__main__':
    main()