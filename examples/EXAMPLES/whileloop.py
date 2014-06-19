#!/usr/bin/env python

while True:
    name = raw_input("Enter a name (or q to quit): ")
    if name == '':
        continue
    if name.lower() == 'q':
        print "goodbye!"
        break
    print "welcome, ",name
