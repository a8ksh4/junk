#!/usr/bin/env python

import inspect

class Spam: pass
def Eggs(foo,bar): pass
a = 'hello'
b = 5
c = 343.32

for thing in (inspect,Spam,Eggs):
    print "%s: Module? %s. Function? %s. Class? %s" % (
        thing.__name__,
        inspect.ismodule(thing),
        inspect.isfunction(thing),
        inspect.isclass(thing),
    )
    
print "Function spec for Eggs:",inspect.getargspec(Eggs)
print
frame_info = inspect.getframeinfo(inspect.currentframe())
print "{0:12} {1}".format('filename', frame_info.filename)
print "{0:12} {1}".format('lineno', frame_info.lineno)
print "{0:12} {1}".format('function', frame_info.function)
print "{0:12} {1}".format('code_context', frame_info.code_context)
print "{0:12} {1}".format('index', frame_info.index)
