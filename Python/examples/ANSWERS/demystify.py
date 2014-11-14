#!/usr/bin/env python

with open("../DATA/mystery","rb") as m:
    bytes = m.read()

print bytes[::2]
