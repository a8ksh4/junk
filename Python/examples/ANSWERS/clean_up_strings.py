#!/usr/bin/env python

def cleanup(s):
    return s.strip().lower()

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

for item in spam:
    print "Before: >{0}< After: >{1}<".format(item,cleanup(item))