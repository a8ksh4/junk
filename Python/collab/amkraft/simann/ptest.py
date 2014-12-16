#!/usr/bin/env python
import multiprocessing as mp
import math

def f(x):
	math.factorial(50000) 
	return x

pool = mp.Pool(mp.cpu_count())
print pool.map(f, range(16))
