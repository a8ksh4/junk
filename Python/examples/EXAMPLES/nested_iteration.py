#!/usr/bin/env python
# (c)2014 John Strickler

people = [
    [ 'Ann', 'Whittier', 'TX' ],
    [ 'Raul', 'Rodriguez', 'NV' ],
    [ 'Jim', 'Benson', 'VA' ],
    [ 'Srini', 'Singh', 'IL' ],
]

for p in people:
    print p[0], p[2]
print

for first_name, last_name, state in people:
    print first_name, state
