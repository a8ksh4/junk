#!/usr/bin/env python

presidents = []
with open('../DATA/presidents.txt') as PRES:
    for line in PRES:
        fields = line.split(':')
        last_name = fields[1]
        first_name = fields[2]
        presidents.append(first_name + ' ' + last_name)

pres_upper = [ p.upper() for p in presidents ]

for pres in pres_upper:
    print pres
