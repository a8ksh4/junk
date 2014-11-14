#!/usr/bin/env python

temp = int(raw_input("Enter the temperature: "))
if temp < 76:
    print "Don't go swimming"

num = int(raw_input("Enter a number: "))
if num > 1000000:
	print num,"is a big number"
else:
	print "your number is",num

hour = int(raw_input("Enter the hour: "))
if hour < 12:
	print "Good morning"
elif hour < 18:
	print "Good afternoon"
elif hour < 23:
	print "Good evening"
else:
	print "You're up late"
