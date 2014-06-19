#!/usr/bin/env python
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

def cuw(astring):
    return astring.strip().lower()
    
for s in spam:
    print "[{0}]".format(cuw(s))
    

