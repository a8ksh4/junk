#!/usr/bin/env python

from datetime import datetime as DateTime

class PrintName(object):
    def __init__(self, old_function):
        self._old_function = old_function
        self.__name__ = self._old_function.__name__

    def __call__( self, *args, **kwargs ):
        print "  ==> Calling function {0} at {1}".format(self._old_function.__name__, DateTime.now())
        return self._old_function( *args, **kwargs )

@PrintName
def hello( greeting, whom ):
    print "%s, %s" % ( greeting, whom )

@PrintName
def goodbye():
    print "Goodbye!"

hello('hello','world')
hello('hi','Earth')
goodbye()
goodbye()
print
print goodbye.__name__