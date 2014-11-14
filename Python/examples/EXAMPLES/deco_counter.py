#!/usr/bin/env python

class CountInvocations(object):
    _COUNT = 0

    def __init__(self, decorated_function):
        self._decorated_function = decorated_function
        self.__name__ = decorated_function.__name__

    def __call__(self, *args, **kwargs):
        CountInvocations._COUNT += 1
        print "{0}: Invocation #{1}".format(
            self._decorated_function.__name__, 
            CountInvocations._COUNT
        )

        return self._decorated_function(*args, **kwargs)   

@CountInvocations
def spam():
    print "Hi from foo"
    
for i in xrange(10):
    spam()