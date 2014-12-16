#!/usr/bin/env python
import numpy, random

def findbest(correct, guesses):
	(bestguess, bestscore) = (guesses[0], size*size*maxval) 
	for guess in guesses:
		newscore = numpy.sum(numpy.abs(correct - guess))
		if newscore < bestscore:
			(bestscore, bestguess) = (newscore, guess)
	return (bestscore, bestguess)

def copyandmutate(start, guesses):
	guesses[0] = numpy.copy(start)
	for c in xrange(1,size):
		guesses[c] = numpy.copy(start)
		(x, y) = (random.randint(0,size-1), random.randint(0,size-1))
		v = guesses[c,x,y] + numpy.random.randint(-3,4)
		guesses[c,x,y] = max(0, min(maxval, v))

def main():
	global size, maxval, guesses, correct
	random.seed(0)
	numpy.random.seed(0)
	(size, maxval) = (35, 20)
	guesses = numpy.random.randint(maxval+1, size=(size, size, size))
	correct = numpy.random.randint(maxval+1, size=(size, size))
	best = findbest(correct, guesses)
	while best[0] != 0:
		copyandmutate(best[1], guesses)
		best = findbest(correct, guesses)

if __name__ == "__main__":
	main()
