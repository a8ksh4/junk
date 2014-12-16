'''
Created on 2009-12-21

@author: drnorris
'''

import stackless, random

class DingDong:
    def __init__(self, chainSize):
        self.chainSize = chainSize
        self.instrChannel = stackless.channel()
        self.chainChannel = [stackless.channel() for i in range(chainSize)]
        self.chain = [None for i in range(chainSize)]
        for nodeID in range(chainSize):
            self.chain[nodeID] = stackless.tasklet(self.nodeFunction)(nodeID,
                                                                      self.instrChannel,
                                                                      self.chainChannel[nodeID],
                                                                      self.chainChannel[(nodeID -1) % self.chainSize],
                                                                      self.chainChannel[(nodeID + 1) % self.chainSize])
    
    def nodeFunction(self, myID, instrChannel, myChannel, lnChannel, rnChannel):
        print myID
        myState = False
        while True:
            todo = instrChannel.receive()
            stackless.schedule()
            
            if todo[0] == 'ret':
                myChannel.send(myState)
            elif todo[0] == 'set':
                if todo[1] == None:
                    myState = myChannel.receive()
                else:
                    myState = todo[1]
            elif todo[0] == 'shiftR':
                if myID % 2 == 0:
                    rnChannel.send(myState)
                    myState = myChannel.receive()
                else:
                    tmp = myChannel.receive()
                    rnChannel.send(myState)
                    myState = tmp
            
            stackless.schedule()
    
    def sendInstruction(self, instruction):
        for i in range(self.chainSize):
            print 'sendInstr', 1
            self.instrChannel.send(instruction)
    
    def clearChain(self):
        for i in range(self.chainSize):
            self.instrChannel.send(['set', False])
    
    def setRandom(self, seed=None):
        random.seed(seed)
        for i in range(self.chainSize):
            self.instrChannel.send(['set', None])
        for i in range(self.chainSize):
            self.chainChannel[i].send(bool(random.randint(0,1)))
    
    def printNice(self):
        print '-----'
        for i in range(self.chainSize):
            self.instrChannel.send(['ret', None])
        for i in range(self.chainSize):
            print self.chainChannel[i].receive()
    
    def shiftRight(self):
        for i in range(self.chainSize):
            self.instrChannel.send(['shiftR', None])
        

if __name__ == '__main__':
    myDD = DingDong(4)
    stackless.run()
    #myDD.sendInstruction('blah')
    myDD.printNice()
    myDD.setRandom()
    myDD.printNice()
    myDD.shiftRight()
    myDD.printNice()
    myDD.shiftRight()
    myDD.printNice()