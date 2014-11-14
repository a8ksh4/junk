#!/usr/bin/env python

import os

def main():
    user = os.getenv("USER")
    count = os.getenv("COUNT")
    print "count is",os.environ['COUNT'],"user is",os.environ['USER']
    print "count is",os.environ.get('COUNT'),"user is",os.environ.get('USER')
    print "count is",count,"user is",user
    print os.path.expandvars("count is $COUNT user is $USER")

if __name__ == '__main__':
    main()


