#!/usr/bin/env python

FRUITS = ['watermelon', 'apple', 'kiwi', 'lime', 'orange', 'cherry',
'banana', 'raspberry', 'grape', 'lemon', 'durian', 'guava', 'mango',
'papaya', 'mangosteen', 'breadfruit']

KV_SEQ = ('red', 5, 'blue', 3, 'yellow', 7, 'purple', 2, 'pink', 8)

EVEN_SLICE = slice(0, None, 2)  #  even elements
ODD_SLICE = slice(1, None, 2)   #  odd elements

def main():
    basic_slices()
    print
    convert_iterable_to_dictionary()
    convert_iterable_to_dictionary_briefer()

def basic_slices():
    s = slice(5)  # first 5
    print FRUITS[s]
    print

    s = slice(-5,None)  # last 5
    print FRUITS[s]
    print

    s = slice(3,8)  #  4th through 8th
    print FRUITS[s]
    print

    s = slice(None,None,2) # every other fruit starting with element 0
    print FRUITS[s]

def convert_iterable_to_dictionary():
    '''build a dictionary from an iterable in k1,v1,k2,v2 order'''
    keys = KV_SEQ[EVEN_SLICE]
    values = KV_SEQ[ODD_SLICE]

    kv_tuples = zip(keys, values)  # generates key/value pairs as tuples
    print "kv_tuples:", kv_tuples

    color_dict = dict(kv_tuples)   # initialize a dictionary from key/value pairs
    print "color_dict:", color_dict

def convert_iterable_to_dictionary_briefer():
    '''Same, but without intermediate variables'''
    color_dict = dict(zip(KV_SEQ[EVEN_SLICE],KV_SEQ[ODD_SLICE]))
    print "color_dict:", color_dict

if __name__ == '__main__':
    main()