#!/usr/bin/env python
import sys

person = 'Bob'
age = 22

print "{0} is {1} years old.".format(person, age)
print "{0}, {0}, {0} your boat".format('row')
print "The {1}-year-old is {0}".format(person, age)
print "{name} is {age} years old.".format(name='Bob',age=22)
print "{name} is {age} years old.".format(name=person,age=age)# only in version 2.7 (and Python 3.x)
if sys.version_info[0] == 2 and sys.version_info[1] == 7:
    print
    print "{} is {} years old.".format(person, age)
    print "{name} is {} and his favorite color is {}".format(22,'blue',name='Bob')