#!/usr/bin/env python

spam = "spam"

def fun_one():
	print "Hello, world"

def fun_two(n):
	return n ** 2

def fun_three(n,*opt):
	print "n is ",n
	print "opt is",opt

def fun_four(**named_args):
	for name in named_args:
		print name,"==> ",named_args[name]

def fun_five(count=3):
	for i in range(count):
		print spam,
	print


fun_one()
x = fun_two(5)
print "fun_two(5) is",x
fun_three('apple',"blueberry","peach","cherry")
fun_four(name="Lancelot",quest="Grail",color="red")
fun_five()
fun_five(5)
