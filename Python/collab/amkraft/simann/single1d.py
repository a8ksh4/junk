import random
import copy
import sys

size = 10
maxval = 9

def compare(correct, guess):
	diff = 0
	for c in range(size):
		diff += abs(correct[c] - guess[c])
	return diff

def findbest(correct, guesses):
	bestscore = compare(correct, guesses[0])
	bestguess = guesses[0]
	for c in range(1,size):
		newscore = compare(correct, guesses[c])
		if newscore < bestscore:
			bestscore = newscore
			bestguess = guesses[c]
	
	return (bestscore, bestguess)

def copyandmutate(starter):
	newguesses = []
	newguesses.append(starter)
	for c in range(size):
		newguess = copy.copy(starter)
		v = random.randint(0,maxval)
		newguess[v] = random.randint(0,maxval)
		newguesses.append(newguess)
	return newguesses

def randomguess():
	return [random.randint(0,maxval) for c in range(size)]

def run():
	guesses = [randomguess() for c in range(size)]
	correct = randomguess()
	print "correct:", correct
	while True:
		best = findbest(correct, guesses)
		sys.stdout.write('.')
		if(best[0] == 0):
			print
			break
		guesses = copyandmutate(best[1])
	print "found:", best[1]

run()
