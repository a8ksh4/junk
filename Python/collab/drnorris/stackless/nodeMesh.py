'''
Created on 2009-12-21

@author: drnorris
'''

import stackless, random

class NodeMeshThing:
    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes
        meshState = [False for i in range(self.numberOfNodes)]
        
        self.instChannel = stackless.channel()
        self.meshChannel = [stackless.channel() for i in range(self.numberOfNodes)]
        
        self.meshNode = [None for i in range(numberOfNodes)]
        
        for node in range(len(self.meshNode)):
            self.meshNode[node] = stackless.tasklet(self.nodeFunction)(node, self.instChannel, self.meshChannel)

    def nodeFunction(self, myID, instChannel, channels):
        self.myState = False
        print myID
        stackless.schedule()
        self.numOfNeighbors = len(channels) - 1
        self.numOfChannels = len(channels)
        
        while True:
            self.todo = instChannel.receive()
            
            if self.todo[0] == 'print':
                print myID, ' - state: ', self.myState
            elif todo[0] == 'get':
                channels[myID].send(myState)
            elif todo[0] == 'set':
                myState = channels[myID].receive()
            elif todo[0] == 'step':
                rCount = 0
                sCount = 0
                chanSentTo = [False for i in range(numOfChannels))]
                
                while True:
                    if rCount < self.numOfNeighbors:
                        for chan in range(len(channels)):
                            if not chan == myID:
                                if chanSentTo[chan] == False:
                                    print myID, '- chan bal:  ', chan, channels[chan].balance
                                    if not channels[nodeNum].balance == 0:
                                        print myID, '- receiving: ', chan
                    if recCount < numNeighbors:
                        for chanNum in range(len(channels)):
                            print myID, '- nStat', chanNum, channels[chanNum].balance

                            if chanNum == myID:
                                continue
                            
                            if chanSentTo[chanNum] == False:
                                if not channels[chanNum].balance == 0:
                                    print myID, '- receiving:', chanNum
                                    if channels[chanNum].receive() == True:
                                        nCount += True
                                    
                                    recCount =+ 1
                                    chanSentTo[chanNum] == True
                                    break
                    
                    if sentCount < numNeighbors:
                        print myID, '- sending'
                        channels[myID].send(myState)
                        sentCount += 1
                        print myID, '- done sending'
                    
                    if sentCount == numNeighbors:
                        if recCount == numNeighbors:
                            print myID, '- done communicating'
                            break
                        
    def stepStates(self):
        for node in range(self.numberOfNodes):
            self.instChannel.send(['step', None])

    def printNodeStates(self):
        print '- - - -'
        for node in range(self.numberOfNodes):
            self.instChannel.send(['print', None])
    
    def getNodeStates(self):
        for node in range(self.numberOfNodes):
            self.instChannel.send(['get', None])
        for node in range(self.numberOfNodes):
            meshState[node] = self.meshChannel[node].receive()
        return meshState
    
    def randomizeStates(self):
        for nodes in range(self.numberOfNodes):
            self.instChannel.send(['set', None])
        for node in range(self.numberOfNodes):
            self.meshChannel[node].send(bool(random.randint(0,1)))
        

if __name__ == '__main__':
    mymesh = NodeMeshThing(2)
    stackless.run()
    
    #mymesh.printNodeStates()
    mymesh.randomizeStates()
    mymesh.printNodeStates()
    #mymesh.randomizeStates()
    #mymesh.printNodeStates()
    print '- - - -'
    mymesh.stepStates()
    #mymesh.printNodeStates()
    