#!/usr/bin/env python
#!/usr/bin/env pypy
import itertools as it
import sys
from copy import deepcopy

BOARD = [[None, None, True, True, True, None, None],
         [None, None, True, True, True, None, None],
         [True, True, True, True, True, True, True],
         [True, True, True, False, True, True, True],
         [True, True, True, True, True, True, True],
         [None, None, True, True, True, None, None],
         [None, None, True, True, True, None, None]]

def listMoves(board):
    moves = []
    for x,y in it.permutations(range(7), 2):
        if not board[x][y]:
            continue
        for xod, yod, xmd, ymd in ( (-2,  0, -1,  0),
                                ( 2,  0,  1,  0),
                                ( 0, -2,  0, -1),
                                ( 0,  2,  0,  1) ):
            move = (x, y, x+xod, y+yod, x+xmd, y+ymd)
            xo, yo, xm, ym = move[2:]
            if xo >= 7 or xo < 0 or yo >= 7 or yo < 0:
                continue
            if None in (board[xo][yo], board[xm][ym]):
                continue
            if board[xo][yo] == False and board[xm][ym] == True:
                moves.append(move)
    return moves

def applyMove(board, move):
    board = deepcopy(board)
    x, y, xo, yo, xm, ym = move
    board[x][y] = False
    board[xm][ym] = False
    board[xo][yo] = True
    return board

def countBoard(board):
    sum = 0
    for row in board:
        #print row
        for col in row:
            if col == True:
                sum += 1
    return sum

def genNext(board, level=0):
    numLeft = countBoard(board)
    #print level, numLeft, " - ", level + numLeft
    if numLeft <= LIMIT:
        print level, numLeft, " - ", level + numLeft
        print MOVES
        #for row in board:
        #    print row
        print "Level was:", level
        #testMoves()
        sys.exit()
    for move in listMoves(board):
        MOVES.append(move)
        genNext(applyMove(board, move), level+1)
        MOVES.pop()

def printBoard(board):
    for row in board:
        print row

def testMoves():
    board = BOARD
    printBoard(board)
    for move in MOVES:
        raw_input()
        print move
        board = applyMove(board, move)
        printBoard(board)


MOVES = [(2,4,4,4,3,4),]
LEVELS = 0
LIMIT = 3
    
if __name__ == '__main__':
    #print countBoard(BOARD, 1)
    genNext(applyMove(BOARD, MOVES[0]), 1)
