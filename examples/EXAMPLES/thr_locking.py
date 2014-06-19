#!/usr/bin/env python

import threading
import random
import time

WORDS = 'apple banana mango peach papaya cherry lemon watermelon fig elderberry'.split()

WORD_LIST = ''   # the threads will append words to this list
WORD_LIST_LOCK = threading.Lock()
STDOUT_LOCK = threading.Lock()

class SimpleThread(threading.Thread):
    def __init__(self, num):
        super(SimpleThread, self).__init__()
        self._num = num
        self._word = WORDS[i]

    def run(self):
        global WORD_LIST

        time.sleep(random.randint(1,3))
        with STDOUT_LOCK:
            print "Hello from thread {0} ({1})".format(self._num, self._word)

        with WORD_LIST_LOCK:
            WORD_LIST += self._word

all_threads = []
for i in range(10):
    t = SimpleThread(i)
    all_threads.append(t)
    t.start()
    
print "All threads launched..."

for t in all_threads:
    t.join()

print WORD_LIST