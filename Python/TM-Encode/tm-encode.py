#!/bin/python

words = {}
words['Dan Norris'] = '01000100011000010110111000100000010011100110111101110010011100100110100101110011'
words['Dan Norris 5302133334'] = '010001000110000101101110001000000100111001101111011100100111001001101001011100110010000000110101001100110011000000110010001100010011001100110011001100110011001100110100'


tape = ''

def getMove(incr):
    increment = incr
    def move():
        new_pos = position + incr
        if new_pos < 0:
            tape = abs(incr)*' ' + tape
            position += abs(incr)
        position += incr
    return move

def getWrite(val):
    value = val
    def write():
        tape[position] = val
    return write

rules = ((0
rules = {}
rules[0] = {0: moveLeft
