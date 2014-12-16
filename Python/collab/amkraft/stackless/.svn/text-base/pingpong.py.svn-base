import stackless

class BoardHandler:
    def __init__(self):
        self.channel = stackless.channel()
        self.valarr = {} 
    def handle(self):
        while 1:
            inst, num, val = self.channel.receive()
            print inst, num, val
            if(inst == 'send'):
                self.valarr[num] = val
            if(inst == 'print'):
                print "valarr = %s" % self.valarr.values()

class Ping:
    def __init__(self, value, num, boardchannel):
        self.value = value
        self.channel = stackless.channel()
        self.instchannel = stackless.channel()
        self.num = num
        self.boardchannel = boardchannel
        self.lneighbor = None
        self.rneighbor = None
        self.neighborcount = 0
        
    def ping(self):
        while 1:
            self.instchannel.receive()
            if(not self.num % 2):
                self.rneighbor.send(self.value)
            else:
                self.neighborcount += self.channel.receive()
            if(not self.num % 2):
                self.lneighbor.send(self.value)
            else:
                self.neighborcount += self.channel.receive()
            if(self.num % 2):
                self.rneighbor.send(self.value)
            else:
                self.neighborcount += self.channel.receive()
            if(self.num % 2):
                self.lneighbor.send(self.value)
            else:
                self.neighborcount += self.channel.receive()
            
            print "cell #%d has %d alive neighbors and is value %d" % (self.num, self.neighborcount, self.value) 
            self.value = self.neighborcount != 0
            
            self.boardchannel.send(['send', self.num, self.value])

board = BoardHandler()
stackless.tasklet(board.handle)()
        
pings = []
count = 4
for c in range(count):
    pings.append(Ping(0, c, board.channel))

for c in range(count):
    pings[c].lneighbor = pings[(c - 1) % count].channel
    pings[c].rneighbor = pings[(c + 1) % count].channel

pings[0].value = 1

for c in range(count):
    stackless.tasklet(pings[c].ping)()

for j in range(1):
    for c in range(count):
        pings[c].instchannel.send(0)
    stackless.run()
    board.channel.send(['print', None, None])
    stackless.run()
