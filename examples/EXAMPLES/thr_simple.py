#!/usr/bin/env python

import threading
import random
import time

class SimpleThread(threading.Thread):
    def __init__(self,num):
        # call base class's __init__() -- required
        super(SimpleThread, self).__init__()
        self._threadnum = num

    # this is what does the actual work
    def run(self):
        time.sleep(random.randint(1,10))
        print "Hello from thread {0}".format(self._threadnum)

for i in range(10):
    t = SimpleThread(i)
    t.start()

print "Done."