#!/usr/bin/env pypy
import itertools as it
import sys
from copy import deepcopy

BASE_BOARD = \
        [[None, None, True, True, True, None, None],
         [None, None, True, True, True, None, None],
         [True, True, True, True, True, True, True],
         [True, True, True, False, True, True, True],
         [True, True, True, True, True, True, True],
         [None, None, True, True, True, None, None],
         [None, None, True, True, True, None, None]]

BOARDS = []
for x in range(33):
    BOARDS.append(deepcopy(BASE_BOARD))

MOVES = [(1,3,3,3,2,3),]
LEVEL = 0
LIMIT = 9

SPOTS = []
for x in range(7):
    for y in range(7):
        SPOTS.append((x, y))
#SPOTS = tuple(it.permutations(range(7), 2))
def listMoves():
    moves = []
    for x,y in SPOTS:
        if not BOARDS[LEVEL][x][y]:
            continue
        for xod, yod, xmd, ymd in ( (-2,  0, -1,  0),
                                ( 2,  0,  1,  0),
                                ( 0, -2,  0, -1),
                                ( 0,  2,  0,  1) ):
            move = (x, y, x+xod, y+yod, x+xmd, y+ymd)
            xo, yo, xm, ym = move[2:]
            if xo >= 7 or xo < 0 or yo >= 7 or yo < 0:
                continue
            if None in (BOARDS[LEVEL][xo][yo], BOARDS[LEVEL][xm][ym]):
                continue
            if BOARDS[LEVEL][xo][yo] == False and BOARDS[LEVEL][xm][ym] == True:
                moves.append(move)
    return moves

def applyMove(move):
    global BOARDS
    #if LEVEL==1:
    #    printBoard(2, ' 2a ')
    #    print SPOTS
    for x,y in SPOTS:
        BOARDS[LEVEL+1][x][y] = BOARDS[LEVEL][x][y]
    #if LEVEL==1:
    #    printBoard(2, ' 2b ')
    x, y, xo, yo, xm, ym = move
    BOARDS[LEVEL+1][x][y] = False
    BOARDS[LEVEL+1][xm][ym] = False
    BOARDS[LEVEL+1][xo][yo] = True
    #if LEVEL==1:
    #    printBoard(2, ' 2c ')

def countBoard(level=False):
    sum = 0
    if level is False:
        level = LEVEL
    for row in BOARDS[level]:
        #print row
        for col in row:
            if col == True:
                sum += 1
    return sum

def genNext():
    global LEVEL, MOVES
    #printBoard()
    numLeft = countBoard()
    #print LEVEL, numLeft, " - ", LEVEL + numLeft, " : ", len(listMoves()),
    if numLeft <= LIMIT:
        print LEVEL, numLeft, " - ", LEVEL + numLeft
        print MOVES
        #for row in board:
        #    print row
        print "Level was:", LEVEL
        testMoves()
        sys.exit()
    for move in listMoves():
        #print move,
        MOVES.append(move)
        applyMove(move)
        LEVEL += 1
        genNext()
        LEVEL -= 1
        MOVES.pop()

def printBoard(level=False, prefix=False):
    if prefix:
        print ''
    if level is False:
        level = LEVEL
    if not prefix:
        prefix = ' ' + str(level) + '  '
    for num, row in enumerate(BOARDS[level]):
        print prefix,
        for item in row:
            if item == True:
                print 1,
            elif item == False:
                print 0,
            else:
                print ' ',
        if num == 0:
            print countBoard(level)
        else:
            print ''

def testMoves():
    for level in range(LEVEL+1):
        print ''
        printBoard(level)

    
if __name__ == '__main__':
    #print countBoard(BOARD, 1)
    LIMIT=1
    LEVEL=0
    printBoard()
    print ''
    applyMove(MOVES[0])
    LEVEL=1
    genNext()
