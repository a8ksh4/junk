#!/usr/bin/env python

'''
    
    
    by John Strickler
    (c) 2013 CJ Associates
'''
from datetime import datetime as DateTime
import time

# September 9, 1941 is Dennis Ritchie's BD. Look him up if you don't know who he is

def main():
    format_time()
    parse_time()

def format_time():
    drbd1 = DateTime(1941, 9, 9)
    now = time.localtime()

    print drbd1.strftime('%m/%d/%y')
    print drbd1.strftime('%B %d, %Y')
    print

    print time.strftime('%m/%d/%y', now)
    print time.strftime('%B %d, %Y', now)
    print

def parse_time():
    s1 = "September 09, 1941"
    s2 = "09/09/41"
    print DateTime.strptime(s1, "%B %d, %Y")
    print DateTime.strptime(s2, "%m/%d/%y")  #oops!

    print time.strptime(s1, "%B %d, %Y")
    print time.strptime(s2, "%m/%d/%y")  #oops!

if __name__ == '__main__':
    main()
