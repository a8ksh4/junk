#!/usr/bin/env python

counts = {}

with open("../DATA/breakfast.txt") as BR: 

    for breakfast_item in BR:
        breakfast_item = breakfast_item.rstrip()
        counts[breakfast_item] = counts.get(breakfast_item,0) + 1

for item,count in counts.iteritems():
    print item,count