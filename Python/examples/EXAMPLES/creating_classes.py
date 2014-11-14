#!/usr/bin/env python

def f1(self):
    print "Hello from f1()"

def f2(self):
    print "Hello from f2()"

new_class = type("new_class", (object,), {
    'hello1': f1,
    'hello2': f2,
    'color': 'red',
    'state': 'Ohio',
})

n1 = new_class()

n1.hello1()
n1.hello2()
print n1.color
print

subclass = type("subclass", (new_class,), {'fruit': 'banana'})
s1 = subclass()
s1.hello1()
print s1.color
print s1.fruit
