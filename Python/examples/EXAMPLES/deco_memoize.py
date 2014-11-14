#!/usr/bin/env python

class Memoize(object):
    
    def __init__(self, old_function):
        self._old_function = old_function
        self._cache = {}
        self.__name__ = old_function.__name__

    def __call__(self, *args, **kwargs):
        if args not in self._cache:
            self._cache[args] = self._old_function(*args)
        
        return self._cache[args]
    
if __name__ == '__main__':
    @Memoize
    def pow2(exp):
        print "Calling pow2 for {0}".format(exp)
        return 2 ** exp

    print "Function name is", pow2.__name__
    print

    for i in 5, 6, 5, 7, 8, 6, 5, 1, 2, 5:
        print "2^{0} is {1}".format(i, pow2(i))