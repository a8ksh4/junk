#!/usr/bin/env python


LIMIT=99
if len(sys.argv) > 1:
    limit = int(sys.argv[1])

values = [ True for val in range(LIMIT+1) ]
primes = []
#print list(enumerate(values))

for addr in range(2, LIMIT+1):
    if values[addr]:
        primes.append(addr)
        for val in xrange(2*addr, LIMIT+1, addr):
            values[val] = False

print primes

