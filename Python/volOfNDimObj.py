#!/usr/bin/env python

''' 
  * Calculate volume of n dimensional object
  * function that takes two lists and finds the distance of those lists 
    two vectors, x, y, and z.  What's teh distance between them... 
'''
import operator
from math import sqrt

def blahdistance(points):
    return reduce(operator.add, 
                map(lambda x: (x[0] - x[1])**2, 
                    zip(*points)))**0.5

   
if __name__ == '__main__':
    points = (
                ((1,), (3,)), 
                ((0, 0), (1, 1)), 
                ((0, 0, 0), (1, 1, 1)),
                ((2, 2, 2, 2), (4, 4, 4, 4)),
                ((0, 0, 0, 0), (0, 0, 0, 1))
             )

    print map(blahdistance, points)
