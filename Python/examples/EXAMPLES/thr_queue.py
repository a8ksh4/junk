#!/usr/bin/env python

import Queue
import random
from threading import Thread,Lock as tlock
import time

NUM_ITEMS = 20000
POOL_SIZE = 100

q = Queue.Queue(0)

shared_result = []
result_lock = tlock()
stdout_lock = tlock()

import random

class Words(object):
    def __init__(self):
        with open('../DATA/words.txt') as WORDS:
            self._words = [ word[:-1] for word in WORDS ]
        self._num_words = len(self._words)
        
    def GetRandomWord(self):
        return self._words[random.randrange(0,self._num_words)]

class Worker(Thread):
    
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        while True:
            try:
                # get data from the queue
                s1 = q.get(block=False)
                stdout_lock.acquire()
                print "{0} fetching {1}".format(self.name,s1)
                stdout_lock.release()
                s2 = s1.upper() + ' '
                result_lock.acquire()
                shared_result.append(s2)
                result_lock.release()

            # quit when there is no more data in the queue
            except Queue.Empty:
                break

# fill the queue
words = Words()
for i in range(NUM_ITEMS):
    w = words.GetRandomWord()
    q.put(w)

start_time = time.ctime()

# populate the threadpool
pool = []
for i in xrange(POOL_SIZE):
    name = "Worker {0:03d}".format(i)
    w = Worker(name)  # add thread to pool
    w.start()
    pool.append(w)
    
for t in pool:
    t.join() # wait for each queue to finish

end_time = time.ctime()

print(shared_result[-50:])
print len(shared_result)
print(start_time)
print(end_time)
