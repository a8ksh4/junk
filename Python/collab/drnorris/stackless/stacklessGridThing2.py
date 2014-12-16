'''
Created on 2009-12-21

@author: drnorris
'''

import stackless, random, time

class StacklessGridThing:
    def __init__(self, gridSize=4):
        self.gridSize = gridSize - gridSize % 2
        self.numberOfNodes = self.gridSize * self.gridSize
        self.grid = [[False for col in range(self.gridSize)] for row in range(self.gridSize)]
        self.gridChannel = [[stackless.channel() for col in range(self.gridSize)] for row in range(self.gridSize)]
        self.instChannel = stackless.channel()
        self.gridNode = [[None for col in range(self.gridSize)] for row in range(self.gridSize)]

        for col in range(gridSize):
            for row in range(gridSize):
                nChannels = []
                for x in range(-1,2):
                    for y in range(-1,2):
                        nChannels.append([self.gridChannel[(col + x) % self.gridSize][(row + y) % self.gridSize], False])
                
                self.gridNode[col][row] = stackless.tasklet(self.nodeFunction)([col, row],
                                                                               self.gridChannel[row][col],
                                                                               self.instChannel,
                                                                               nChannels)

    def nodeFunction(self, myID, myChannel, instChannel, nChannels):
        myState = False
        while True:
            stackless.schedule()
            todo = instChannel.receive()
            
            if todo[0] == 'set':
                if todo[1] == None:
                    myState = myChannel.receive()
                else:
                    myState = todo[1]
            
            elif todo[0] == 'blah':
                print myID
            
            elif todo[0] == 'get':
                if not todo[1] == None:
                    if todo[1] == myID:
                        myChannel.send(myState)
                else:
                    myChannel.send(myState)
                
            elif todo[0] == 'step':
                nCount = 0
                print myID
                
                for neighbor in range(len(nChannels)):
                    nChannels[neighbor][1] = False
                    
                for eachNeighbor in range(8):
                    for neighbor in range(len(nChannels)):
                        if nChannels[neighbor][1] == False:
                            if not nChannels[neighbor][0].balance == 0:
                                if nChannels[neighbor][0].receive() == True:
                                    nCount += 1
                                nChannels[neighbor][1] = True
                                #break
                    myChannel.send(myState)
                    stackless.schedule
                
                if myState == True:
                    if not 2 <= nCount <= 3:
                        myState == False
                else:
                    if nCount == 3:
                        myState == True

    def setNodeState(self, col, row, newState):
        for nodes in range(self.numberOfNodes):
            self.instChannel.send(['set', [col, row]])

        self.nodeChannel[col][row].send(newState)
    
    def getState(self):
        for nodes in range(self.numberOfNodes):
            self.instChannel.send(['get', None])

        for col in range(self.gridSize):
            for row in range(self.gridSize):
                self.grid[col][row] = self.gridChannel[col][row].receive()

        return self.grid
        
    def step(self, numOfIterations=1):
        for nodes in range(self.numberOfNodes):
            self.instChannel.send(['step', None])
   
    def clear(self):
        for nodes in range(self.numberOfNodes):
            self.instChannel.send(['set', False])

    def randomize(self, seed=None):
        for nodes in range(self.numberOfNodes):
            self.instChannel.send(['set', None])

        random.seed(seed)
        for col in range(self.gridSize):
            for row in range(self.gridSize):
                self.gridChannel[col][row].send(bool(random.randint(0, 1)))
    
    def doNothing(self):
        count = 0
        for nodes in range(self.numberOfNodes):
            print count
            count += 1
            self.instChannel.send(['blah', None])
    
    def printNice(self):
        print '- - - - -'
        for row in self.getState():
            print row                
            
            

if __name__ == '__main__':
    mygrid = StacklessGridThing(4)
    stackless.run()
    #mygrid.doNothing()
    mygrid.printNice()
    mygrid.randomize(1)
    mygrid.printNice()
    mygrid.step()
    mygrid.doNothing()
    #mygrid.printNice()


        
