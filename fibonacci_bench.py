#!/usr/bin/env python

import time
from collections import OrderedDict

def standardFib(count):
    seq = [0, 1]
    while len(seq) < count:
        seq.append(seq[-1] + seq[-2])
    return sum(seq)

def fibRecurs__(n):
    return n if n < 2 else fibRecurs__(n-2) + fibRecurs__(n-1)

__fib_cache = {}
def fib________(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib________(n-2) + \
                                         fib________(n-1)
        return __fib_cache[n]

def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fibMemo____(n):
    return n if n < 2 else fibMemo____(n-2) + fibMemo____(n-1)

if __name__ == '__main__':
    clock = OrderedDict()
    count = 24
    for func in (standardFib, fibRecurs__, fib________, fibMemo____):
        clock[func.__name__] = {}
        stime = time.time()
        clock[func.__name__]["result"] = func(count)
        etime = time.time()
        clock[func.__name__]["runTime"] = '{0:.10f}'.format(etime - stime)

    for item in clock.keys():
        print (item[:11], clock[item])
