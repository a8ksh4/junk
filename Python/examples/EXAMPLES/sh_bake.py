#!/usr/bin/env python

from sh import netstat

ns = netstat.bake('-an')

print ns()

