#!/usr/bin/env python


import sys
import signal

class Barf():
    def __init__(self):
        signal.signal(signal.SIGINT, signal.signal_handler)
        
    def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

    def blah(self):
        while True:
            sleep(10)


if __name__ == '__main__':
    barf = Barf()

    

    print 'Press Ctrl+C'
    #signal.pause()
