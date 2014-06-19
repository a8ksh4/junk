#!/usr/bin/env python

knight_info = {}

with open("../DATA/knights.txt") as kn:
    for line in kn:
        (name,title,color,quest,comment) = line[:-1].split(":")
        knight_info[name] = [title,color,quest,comment]

for name,info_list in knight_info.iteritems():
    print "name:",name,"title:",info_list[0]