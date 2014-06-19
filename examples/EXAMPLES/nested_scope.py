#!/usr/bin/env python

x = 42

def fun_A():
    x = 5
    
    def fun_B():
        global x
        x = 32
        return x

    print 'function A -- x is',x

    return fun_B;

f = fun_A()

print f()
print 'main -- x is',x
