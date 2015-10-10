#!/usr/bin/env python
import itertools as it

board = [[None, None, None, True, True, True, None, None, None],
         [None, None, None, True, True, True, None, None, None],
         [None, None, None, True, True, True, None, None, None],
         [True, True, True, True, True, True, True, True, True],
         [True, True, True, True, False, True, True, True, True],
         [True, True, True, True, True, True, True, True, True],
         [None, None, None, True, True, True, None, None, None],
         [None, None, None, True, True, True, None, None, None],
         [None, None, None, True, True, True, None, None, None]]

def listMoves(board):
    moves = []
    for x,y in it.permutations(range(9), 2):
        if not board[x][y]:
            continue
        for xod, yod, xmd, ymd in ( (-2,  0, -1,  0),
                                ( 2,  0,  1,  0),
                                ( 0, -2,  0, -1),
                                ( 0,  2,  0,  1) ):
            move = (x, y, x+xod, y+yod, x+xmd, y+ymd)
            xo, yo, xm, ym = move[2:]
            if xo >= 9 or xo < 0 or yo >= 9 or yo < 0:
                continue
            if None in (board[xo][yo], board[xm][ym]):
                continue
            if board[xo][yo] == False and board[xm][ym] == True:
                moves.append(move)
    return moves

def applyMove(board, move):
    x, y, xo, yo, xm, ym = move
    board[x][y] = False
    board[xm][ym] = False
    board[xo][yo] = True
    return board

def genNext(field, level=0):
    print field['board']
    if level == DONE:
        BREAK = True

    rawread('next')

    for move in listMoves(field['board']):
        if BREAK:
            break
        new = {'board': applMove(field['board']), 'sub':{} }
        field['sub'][move] = genNext(new, level+1)
    return field

base_move = (2,4,4,4,3,4)
field = {'board': applMove(board, base_move), 'sub':{} }
BREAK = False
LEVELS = 0
DONE = 41
    
if __name__ == '__main__':
    print listMoves(board)
