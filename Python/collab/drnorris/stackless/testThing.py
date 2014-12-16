import stackless

class TestThing:
    def __init__(self, numOfNodes):
        self.numOfNodes = numOfNodes
        self.chan = [stackless.channel() for i in range(self.numOfNodes)]
        self.node = [None for i in range(self.numOfNodes)]
        for nodeNum in range(self.numOfNodes):
            self.node[nodeNum] = stackless.tasklet(self.nodeFunction)(nodeNum, self.chan)

    def nodeFunction(self, myID, channels):
        print myID
        stackless.schedule()
        rCount = 0
        sCount = 0
        numOfNeighbors = len(channels) - 1
        nCommTrack = [False for i in range(len(channels))]
        while True:
            if rCount < numOfNeighbors:
                for nodeNum in range(len(channels)):
                    if not nodeNum == myID:
                        if nCommTrack[nodeNum] == False:
                            print myID, '- chan bal:  ', nodeNum, channels[nodeNum].balance
                            if not channels[nodeNum].balance == 0:
                                print myID, '- receiving: ', nodeNum, channels[nodeNum].receive()
                                rCount += 1
                                nCommTrack[nodeNum] = True
                        
            if sCount < numOfNeighbors:
                print myID, '- sending'
                channels[myID].send(myID)
                sCount += 1
            
            print myID, '- comm count:', rCount, sCount
            if rCount == numOfNeighbors:
                if sCount == numOfNeighbors:
                    print myID, '- all done'
                    break

if __name__ == '__main__':
    mything = TestThing(3)
    stackless.run()