#!/usr/bin/env python

VALUES = ( 15, 5, 'ni!')

def main():
    # tedious way
    ni(VALUES[0], VALUES[1], VALUES[2])

    print

    # pythonic way
    ni(*VALUES)

def ni(num_knights,repeat_count,silly_word):
    print "We are the {0} knights who say {1}".format(num_knights, silly_word)
    for i in range(repeat_count):
        print silly_word,
    print

if __name__ == '__main__':
    main()