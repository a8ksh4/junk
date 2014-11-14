#!/usr/bin/env python

import time

def main():
    right_now = time.time()
    print "It is {0} seconds since 1/1/70".format(right_now)
    print
    time.sleep(2)
    then_ctime = time.ctime(right_now)
    print "it was", then_ctime

    now_asc = time.asctime()
    print "then it was",now_asc

    time.sleep(3)

    now_ctime = time.ctime()
    print "it is now",now_ctime

if __name__ == '__main__':
    main()