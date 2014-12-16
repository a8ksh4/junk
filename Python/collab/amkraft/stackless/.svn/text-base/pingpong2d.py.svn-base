import stackless
import sys

class BoardHandler:
    def __init__(self, count):
        self.count = count
        self.channel = stackless.channel()
        self.valarr = [[ -1 for i in range(self.count) ] for k in range(self.count)]
        self.pings = []
        stackless.tasklet(self.handle)()
        self.initboard()

    def handle(self):
        while 1:
            inst, num, val = self.channel.receive()
            if(inst == 'send'):
                self.valarr[num[0]][num[1]] = val
            if(inst == 'print'):
                print self.valarr

    def mainloop(self):
        for j in range(2):
            for y in range(self.count):
                for x in range(self.count): 
                    self.pings[y*self.count+x].instchannel.send(0)
            stackless.run()
            self.channel.send(['print', None, None])
            stackless.run()
 
    def initboard(self):
        for y in range(self.count):
            for x in range(self.count): 
                self.pings.append(Ping(0, [x,y], self.channel))
        
        for y in range(self.count):
            for x in range(self.count):
                for iy in range(-1, 2):
                    for ix in range(-1, 2):
                        if( ix == 0 and iy == 0):
                            continue
                        ax = (x + ix) % self.count
                        ay = (y + iy) % self.count
                        ch = self.pings[ay * self.count + ax].channel
                        self.pings[y * self.count + x].neighbors.append(ch)
        
        for y in range(self.count):
            for x in range(self.count): 
                stackless.tasklet(self.pings[y*self.count+x].ping)()

    def loadtestboard(self):
        self.pings[self.count].value = 1
        self.pings[self.count+1].value = 1
        self.pings[self.count+2].value = 1

class Ping:
    def __init__(self, value, num, boardchannel):
        self.value = value
        self.channel = stackless.channel()
        self.instchannel = stackless.channel()
        self.num = num
        self.boardchannel = boardchannel
        self.neighbors = []

    def handleQuad(self, ox, oy):
        if(ox and oy):
            for c in range(8):
                self.neighbors[c].send(self.value)
        else:
            d = 0
            if((not ox) and (not oy)):
                d = 4
            else:
                d = 2
            for c in range(d):
                self.neighborcount += self.channel.receive()

    def ping(self):
        while 1:
            self.instchannel.receive()
            self.neighborcount = 0
            ox = self.num[0] % 2
            oy = self.num[1] % 2
            
            self.handleQuad(ox, oy)
            self.handleQuad(ox, not oy)
            self.handleQuad(not ox, oy)
            self.handleQuad(not ox, not oy)
            
            if(self.neighborcount == 3):
                self.value = 1
            elif(self.neighborcount < 2 or self.neighborcount > 3):
                self.value = 0
            
            self.boardchannel.send(['send', self.num, self.value])
        
board = BoardHandler(4)
board.loadtestboard()
board.mainloop()