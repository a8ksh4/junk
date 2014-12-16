#!/usr/bin/env python

import sys

def printGrid(grid):
	for y in range(len(grid)):
		print "[",
		for x in range(len(grid[0])):
			if(grid[x][y]):
				sys.stdout.write("O")
			else:
				sys.stdout.write("_")
		print "]"

def randomGrid(gridSize, x=None):
	rand = random.Random(x)
	return [[rand.randint(0,1) == 1 for col in range(gridSize)] for row in range(gridSize)]

def emptyGrid(gridSize):
	return [[False for col in range(gridSize)] for row in range(gridSize)]

if __name__ == "__main__":
	grid = emptyGrid(3)
