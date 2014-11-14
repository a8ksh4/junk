#!/usr/bin/env python

from itertools import islice, takewhile

def generator():
    i = 1
    while True:
        yield i
        i += 1

def take(n, iterable):
    "Return first n items of the iterable as list"
    return list(islice(iterable, n))

def primes():
    for n in generator():
        if not any(p !=n and n%p == 0 
                   for p in takewhile(lambda x: n>x, primes())):
            yield n

if __name__ == '__main__':
    print take(5, generator())
    print take(10, primes())
