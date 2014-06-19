#!/usr/bin/env python

class Spam(object):

    def __init__(self):
        self.hovercraft = 'eels'

    def eggs(self, egg_method):
        print egg_method, "eggs!"
        
s = Spam()

h = getattr(s,'hovercraft')
print 's.hovercraft:', h


if hasattr(s,'eggs'):
    s.eggs("fried")
    e  = getattr(s,'eggs')
    e("scrambled")

def toast(self, toast_prefix):
    print toast_prefix, "toast!"
    
setattr(Spam,'eggs',toast)  # monkey patch! replace Spam.eggs() with toast()

s.eggs("buttered")   # now really calling toast()

delattr(Spam,'eggs')

if hasattr(Spam, 'eggs'):
    s.eggs("shirred")
else:
    print "Spam does not have eggs"

