#!/usr/bin/env python

pythons = ['Idle','Chapman','Cleese','Jones','Gilliam','Palin']
fawlty = ['Cleese','Cleveland']

p = set(pythons)
p.add('Innes')

f = frozenset(fawlty)

print "p",p
print "f",f
print "p&f",p&f
print "p|f",p|f
print "p^f",p^f
print "p-f",p-f
