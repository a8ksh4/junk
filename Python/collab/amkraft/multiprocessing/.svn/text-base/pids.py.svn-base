#!/usr/bin/env python
import multiprocessing

class Inst:
    d = ["INIT", "TALK", "QUIT", "PRINT", "SETCELL", "NOOP",
         "GETSEGMENT", "GETCELL"]
    INIT, TALK, QUIT, PRINT, SETCELL, NOOP, GETSEGMENT, GETCELL = range(len(d))
    @staticmethod
    def str(inst):
        return Inst.d[inst]

class SegmentComm:
    def __init__(self, dataconn):
        self.dataconn = dataconn
        self.instp, self.instc = multiprocessing.Pipe()
        self.proc = multiprocessing.Process(target=segrun, args=(self.instc, self.dataconn))
class Board:
    def __init__(self, numsegments, segmentsize):
        self.segmentsize = segmentsize
        self.numsegments = numsegments
        p, c = multiprocessing.Pipe()
        self.segments = [SegmentComm(p), SegmentComm(c)]
    def sendall(self, instdata):
        for i in range(self.numsegments):
            self.segments[i].instp.send(instdata)
    def setcell(self, x, y, value):
        if x < self.segmentsize/2:
            self.segments[0].instp.send([Inst.SETCELL, [x, y, value]])
            self.segments[1].instp.send([Inst.NOOP])
    def printgrid(self, num, grid, segmentsizex, segmentsizey):
        print "grid %s" % num
        for y in range(segmentsizey):
            for x in range(segmentsizex):
                print grid[x][y],
            print
    def getgrid(self):
        self.sendall([Inst.GETSEGMENT])
        grid, sizex, sizey = self.segments[0].instp.recv()
        grid2, sizex2, sizey2 = self.segments[1].instp.recv()
        self.printgrid(0, grid, sizex, sizey)
        self.printgrid(1, grid2, sizex2, sizey2)
    def run(self):
        for i in range(self.numsegments):
            self.segments[i].proc.start()
            self.segments[i].instp.send([Inst.INIT, [i, self.segmentsize/2, self.segmentsize]])
        self.setcell(1, 0, 1)
#        self.sendall([Inst.PRINT])
        self.getgrid()
        self.sendall([Inst.QUIT])
        for i in range(self.numsegments):
            self.segments[i].proc.join()
#    def getcell(self, x, y):
#        if x < self.segmentsize/2:
#            self.segments[0].instp.send([Inst.SETCELL, [x, y, value]])
#            self.segments[1].instp.send([Inst.NOOP])

def segrun(instconn, dataconn):
    grid = None
    neighbors = None
    num = None
    segmentsizex, segmentsizey = None, None
    while True:
        comm = instconn.recv()
        inst = comm[0]
        if(len(comm) == 2):
            data = comm[1]
        if inst == Inst.INIT:
            num, segmentsizex, segmentsizey = data
            grid = [[0 for j in range(segmentsizey)] for i in range(segmentsizex)]
            neighbors = [[0 for j in range(segmentsizey)] for i in range(segmentsizex)]
        elif inst == Inst.TALK:
            if(not num % 2):
                dataconn.send("hello from segment %s" % num)
                print dataconn.recv()
            else:
                print dataconn.recv()
                dataconn.send("hello from segment %s" % num)
        elif inst == Inst.QUIT:
            dataconn.close()
            instconn.close()
            return
        elif inst == Inst.PRINT:
            print "segment num: %s" % num
            for y in range(segmentsizey):
                for x in range(segmentsizex):
                    print grid[x][y],
                print
        elif inst == Inst.SETCELL:
            x, y, value = data
            grid[x][y] = value
        elif inst == Inst.GETSEGMENT:
            instconn.send([grid, segmentsizex, segmentsizey])
        elif inst == Inst.NOOP:
            pass

if __name__ == "__main__":
    board = Board(numsegments=2, segmentsize=4)
    board.run()
