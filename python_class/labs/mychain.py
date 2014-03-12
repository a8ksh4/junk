"""
Implement a function called "chain".

Chain takes an arbitrary number or iterables and returns
an iterator over all the data sources so that:

>>> for val in chain([1,2,3], 'abc', [4,5]):
...     print val
1
2
3
a
b
c
4
5


Implement a function called myrange that takes a stop argument and
generates the numbers up to stop. This is a more efficient version of
range() in a for loop:

>>> for i in myrange(4):
...     print i
0
1
2
3

"""
