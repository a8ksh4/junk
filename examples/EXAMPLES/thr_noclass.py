#!/usr/bin/env python

import threading
import random
import time

# function to launch in each thread    
def doit(num):
    time.sleep(random.randint(1,10))
    print "Hello from thread {0}".format(num)

for i in range(10):
    t = threading.Thread(target=doit,args=(i,))
    t.start()
