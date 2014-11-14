#!/usr/bin/env python

spam = 42

def eggs(how):
    name = 'Lancelot'
    favcolor = 'red'
    print "GLOBALS:",globals()
    print
    print "LOCALS:",locals()

eggs('fried')

