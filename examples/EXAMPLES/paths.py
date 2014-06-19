#!/usr/bin/env python

import sys
import os.path

UNIX_PATH_1 = "/usr/local/bin/foo"
UNIX_PATH_2 = "bin/foo.txt"

WIN_PATH_1 = r"\\marmoset\sharing\technology\docs\myproject\intro.doc"
WIN_PATH_2 = r"myproject\intro.doc"

def main():
    if sys.platform == 'win32':
        win_examples()
    else:
        unix_examples()

def unix_examples():
    print "dirname(UNIX_PATH_1): ",os.path.dirname(UNIX_PATH_1)
    print "dirname(UNIX_PATH_2): ",os.path.dirname(UNIX_PATH_2)
    print "basename(UNIX_PATH_1): ",os.path.basename(UNIX_PATH_1)
    print "basename(UNIX_PATH_2): ",os.path.basename(UNIX_PATH_2)
    print 'expanduser("~"): ',os.path.expanduser("~")
    print 'expanduser("~jstrick"): ',os.path.expanduser("~jstrick")
    print "isabs(UNIX_PATH_1): ",os.path.isabs(UNIX_PATH_1)
    print "isabs(UNIX_PATH_2): ",os.path.isabs(UNIX_PATH_2)
    print "os.path.split(UNIX_PATH_1) Head: {0} Tail: {1}".format(*os.path.split(UNIX_PATH_1))
    print "os.path.split(UNIX_PATH_2) Head: {0} Tail: {1}".format(*os.path.split(UNIX_PATH_2))

def win_examples():
    print "dirname(WIN_PATH_1): ",os.path.dirname(WIN_PATH_1)
    print "dirname(WIN_PATH_2): ",os.path.dirname(WIN_PATH_2)
    print "basename(WIN_PATH_1): ",os.path.basename(WIN_PATH_1)
    print "basename(WIN_PATH_2): ",os.path.basename(WIN_PATH_2)
    print "os.path.split(WIN_PATH_1) Head: {0} Tail: {1}".format(os.path.split(WIN_PATH_1))
    print "os.path.split(WIN_PATH_1) Head: {0} Tail: {1}".format(os.path.split(WIN_PATH_2))
    print "os.path.splitunc(WIN_PATH_1) Head: {0} Tail: {1}".format(os.path.splitunc(WIN_PATH_1))
    print "os.path.splitunc(WIN_PATH_1) Head: {0} Tail: {1}".format(os.path.splitunc(WIN_PATH_2))

if __name__ == '__main__':
    main()