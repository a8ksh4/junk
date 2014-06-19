#!/usr/bin/env python

def AddHello(old_class):
    def hello_(self):
        print "Hello!"
        
    old_class.hello = hello_
    return old_class

def AddHex(old_class):
    old_class.__hex__ = lambda self: 'I am cursed!'
    return old_class

def AddPow(old_class):
    old_class.__pow__ = lambda self, x:'I feel {0} times stronger!'.format(x)
    return old_class

if __name__ == '__main__':

    @AddHello
    @AddPow
    @AddHex
    class Spam(object):
        """ 'Empty' class"""
        pass
    
    s = Spam()
    
    s.hello()
    print hex(s)
    print pow(s,10)
