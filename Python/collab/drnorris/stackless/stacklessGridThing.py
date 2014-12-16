'''
Created on 2009-12-21

@author: drnorris
'''

import stackless, random, time

class StacklessGridThing:
    def __init__(self, gridSize=4, gridWrap=True, history=0):
        def checkWrap(pos):
            return pos % self.gridSize

        self.gridSize = gridSize - gridSize % 2
        self.gridWrap = gridWrap
        self.ruleList = [['Game of Life', [3], [2,3]], ['High Life', [3,6], [2,3]]]
        self.setEffectiveRule(0)
        self.grid = [[False for col in range(self.gridSize)] for row in range(self.gridSize)]
        self.gridChannel = [[stackless.channel() for col in range(self.gridSize)] for row in range(self.gridSize)]
        self.instChannel = [[stackless.channel() for col in range(self.gridSize)] for row in range(self.gridSize)]
        self.gridNode = [[None for col in range(self.gridSize)] for row in range(self.gridSize)]
        
        self.blahTasklet = stackless.tasklet(self.blahTaskletFunction)()

        for col in range(gridSize):
            for row in range(gridSize):
                if col % 2 == 1:
                    cellOffsetA = True
                else:
                    cellOffsetA = False
                if row % 2 == 1:
                    cellOffsetB = True
                else:
                    cellOffsetB = False
                self.gridNode[row][col] = stackless.tasklet(self.nodeFunction)(self.gridChannel[row][col], self.instChannel[row][col], 
                                                                          [self.gridChannel[checkWrap(row + 1)][checkWrap(col - 1)],
                                                                           self.gridChannel[checkWrap(row + 1)][checkWrap(col + 1)],
                                                                           self.gridChannel[checkWrap(row + 1)][checkWrap(col)],
                                                                           self.gridChannel[checkWrap(row)][checkWrap(col + 1)],
                                                                           self.gridChannel[checkWrap(row - 1)][checkWrap(col + 1)],
                                                                           self.gridChannel[checkWrap(row - 1)][checkWrap(col - 1)],
                                                                           self.gridChannel[checkWrap(row - 1)][checkWrap(col)],
                                                                           self.gridChannel[checkWrap(row)][checkWrap(col -1)]],
                                                                          self.gridWrap, cellOffsetA, cellOffsetB)
    def blahTaskletFunction(self):
        while True:
            stackless.schedule()

    def nodeFunction(self, myChannel, instChannel, nChannel, gridWrap, offsetA, offsetB):
        myState = False
        #print offsetA, offsetB
        while True:
            nCount = 0
            print 'recieving'
            todo = instChannel.receive()
            print todo
            if todo[0] == 'set':
                myState = todo[1]
                
            elif todo[0] == 'step':
                for count in range(8):
                    if count % 2 == 0:
                        if offsetA == True:
                            if myChannel.recieve() == True:
                                nCount += 1
                            nChannel[count].send(myState)
                        else:
                            nChannel[count].send(myState)
                            if myChannel.recieve() == True:
                                nCount += 1
                    else:
                        if offsetB == True:
                            if myChannel.recieve() == True:
                                nCount += 1
                            nChannel[count].send(myState)
                        else: 
                            nChannel[count].send(myState)
                            if myChannel.recieve() == True:
                                nCount += 1
                            offsetA = True
                    stackless.schedule()

            elif todo[0] == 'get':
                print 'get'
                instChannel.send(myState)
                
            stackless.schedule()

    def setNodeState(self, col, row, newState):
        self.instChannel[col][row].send(['set', newState])
        
    def getCellState(self, col, row):
        self.instChannel[col][row].send(['get', None])
        return self.instChannel[col][row].receive()
    
    def getState(self):
        for col in range(self.gridSize):
            for row in range(self.gridSize):
                self.grid[col][row] = self.getCellState(col, row)
        return self.grid
        
    def step(self, numOfIterations=1):
        for col in range(self.gridSize):
            for row in range(self.gridSize):
                print col, row
                self.instChannel[col][row].send(['step', numOfIterations])
   
    def clear(self):
        for col in range(self.gridSize):
            for row in range(self.gridSize):
                self.setNodeState(col, row, False)

    def randomize(self, seed=None):
        random.seed(seed)
        for col in range(self.gridSize):
            for row in range(self.gridSize):
                self.setNodeState(col, row, bool(random.randint(0,1)))

    def setEffectiveRule(self, ruleNumber):
        self.effectiveRule = ruleNumber
        self.birthValues = self.ruleList[ruleNumber][1]
        self.liveValues = self.ruleList[ruleNumber][2]
    
    def printNice(self):
        for row in self.getState():
            print row                
            
            

if __name__ == '__main__':
    mygrid = StacklessGridThing(4, True, 0)
    stackless.run()
    mygrid.randomize(1)
    mygrid.printNice()
    print '- - - -'
    mygrid.step()
    mygrid.printNice()


        
