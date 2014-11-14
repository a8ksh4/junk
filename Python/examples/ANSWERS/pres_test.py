#!/usr/bin/env python
import pres

print 'PRESIDENT 26:'
for k,v in sorted(pres.get_info(26).iteritems()):
    print k,v
print

print 'PRESIDENT 35:'
for k,v in sorted(pres.get_info(35).iteritems()):
    print k,v
print

oldster = pres.get_oldest()
print "Oldest is",oldster["firstname"],oldster["lastname"] 

youngster = pres.get_youngest()
print "Youngest is",youngster["firstname"],youngster["lastname"] 
