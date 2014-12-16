#!/usr/bin/env python
import multiprocessing as mp, numpy as np, random, sys

def getscore(guess):
	return np.sum(np.abs(correct - guess))

def findbest(guesses):
	m = map(getscore, guesses)
	guessnum = np.argmin(m)
	return (m[guessnum], guesses[guessnum])

def findbestsplit(guesses):
        newguesses = np.copy(guesses)
	loopcount = 10
	for x in xrange(loopcount):
		best = findbest(newguesses)
		if best[0] == 0:
			break
		copyandmutate(best[1], newguesses)
	return best

def mapbestsplit(guesses):
	m = map(findbestsplit, guesses)
	m2 = np.transpose(m)
	guessnum = np.argmin(m2[0])
	return (m[guessnum][0], m[guessnum][1])

def copyandmutate(start, guesses):
	guesses[0] = np.copy(start)
	for c in xrange(1,size):
		guesses[c] = np.copy(start)
		(x, y) = (random.randint(0,size-1), random.randint(0,size-1))
		v = guesses[c,x,y] + np.random.randint(-3,4)
		guesses[c,x,y] = max(0, min(maxval, v))

def main():
	global size, maxval, correct, pool
	(size, maxval) = (35, 20)
	random.seed(0)
	np.random.seed(0)
	guesses = np.random.randint(maxval+1, size=(size, size, size))
	correct = np.random.randint(maxval+1, size=(size, size))
	pool = mp.Pool(mp.cpu_count())
	while True:
		best = mapbestsplit(guesses)
		if best[0] == 0:
			break
		copyandmutate(best[1], guesses)

if __name__ == "__main__":
	main()
