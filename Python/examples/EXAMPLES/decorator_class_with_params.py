#!/usr/bin/env python

from datetime import datetime as DateTime
from functools import wraps

class PrintName(object):
    def __init__(self, printdate=True):
        self._printdate = printdate

    def __call__( self, old_function):

        @wraps(old_function)
        def _new(*args,**kwargs):
            if self._printdate:
                print "  ==> Calling function {0} at {1}".format(old_function.__name__, DateTime.now())
            else:
                print "  ==> Calling function {0}".format(old_function.__name__)

            return old_function(*args,**kwargs)

        return _new

@PrintName()
def hello( greeting, whom ):
    print "%s, %s" % ( greeting, whom )

@PrintName(False)
def goodbye():
    print "Goodbye!"

@PrintName(True)
def hiya():
    print "Hiya!!"

hello('hello','world')
hello('hi','Earth')
goodbye()
goodbye()
hiya()