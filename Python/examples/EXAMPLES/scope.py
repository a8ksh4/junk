#!/usr/bin/env python

x = 5

def spam():
	x = 22   # does not set global x
	print "spam(1)",x
	y = "wolverine"
	print "spam(2)",y

def eggs():
	global x
	print "eggs(1)",x
	x = "wolverine"
	print "eggs(2)",x

spam()
eggs()
print "x is ",x
