#!/usr/bin/env python

class Spam(object):
    
    def __init__(self,name):
        self._name = name
    
    def eggs(self):
        print "Good morning, %s. Here are your delicious fried eggs." % (self._name,)

s = Spam('Mrs. Higgenbotham')
s.eggs()

def scrambled(self):
    print "Hello, %s. Enjoy your scrambled eggs" % (self._name,)
    
Spam.eggs = scrambled   # monkey patch the class

s.eggs()