#!/usr/bin/env python

def pres_upper():
    with open('../DATA/presidents.txt') as PRES:
        for line in PRES:
            # trim line, make it upper case, split on ':',
            # then grab fields 1 through 2
            lname, fname = line[:-1].upper().split(':')[1:3]
        
            # yield (return) "Firstname Lastname"
            yield '{0} {1}'.format(fname,lname)

for pres in pres_upper():
    print pres
    
    
