'''
Created on 2009-12-21

@author: drnorris
'''

import stackless

class StacklessGridThing:
    def __init__(self, gridSize=4):
        self.gridSize = gridSize - gridSize % 2
        self.numberOfNodes = self.gridSize * self.gridSize
        self.grid = [[False for col in range(self.gridSize)] for row in range(self.gridSize)]
        self.instChannel = stackless.channel()
        
        self.gridNode = [[None for col in range(self.gridSize)] for row in range(self.gridSize)]
        for col in range(gridSize):
            for row in range(gridSize):
                self.gridNode[col][row] = stackless.tasklet(self.nodeFunction)([col, row], self.instChannel)

    def nodeFunction(self, myID, instChannel):
        while True:
            todo = instChannel.receive()
            if todo[0] == 'blah':
                print myID
   
    def doNothing(self):
        count = 0
        for nodes in range(self.numberOfNodes):
            print count
            count += 1
            self.instChannel.send(['blah', None])

if __name__ == '__main__':
    mygrid = StacklessGridThing(4)
    stackless.run()
    mygrid.doNothing()



        
