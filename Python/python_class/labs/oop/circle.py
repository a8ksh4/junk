"""
Properties let us intercept attribute access, sneaking in a function
call where it looks like we merely lookup or set an attribute on an
object.

The Circle class below is broken: its constructor takes a radius
argument

>>> c = Circle(radius=10)

and calculates the diameter

>>> c.diameter
20

But what if you changed the radius? Now the diameter would be incorrect!

Fix the class so that the diameter and radius are kept in sync.

>>> c.radius = 5
>>> c.diameter
10
>>> c.diameter = 12
>>> c.radius
6

"""


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
