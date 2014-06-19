#!/usr/bin/env python

from functools import wraps
from datetime import datetime as DateTime

def print_name( old_func ):

    @wraps(old_func)
    def new_func( *args, **kwargs ):
        print "  ==> Calling function {0} at {1}".format(old_func.__name__, DateTime.now())
        return old_func( *args, **kwargs )  # call the 'real' function

    return new_func   # return the new function object


@print_name
def hello( greeting, whom ):
    print "%s, %s" % ( greeting, whom )

@print_name
def goodbye():
    print "Goodbye!"

hello('hello','world')
hello('hi','Earth')
goodbye()
goodbye()
print
print goodbye.__name__