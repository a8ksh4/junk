
import random, math

class sigmoidNeuron:
    def __init__(self, connectedNeurons):
        self.myConnectedNeurons = connectedNeurons
        self.connBias = [self.getRand() for I in range(len(self.myConnectedNeurons))]
        self.myThreshold = 1
        self.myOutput = 1
    
    def getRand(self):
        mu = 0
        sigma = .3
        return random.gauss(mu, sigma)
    
    def addConnection(self, connection):
        self.myConnections.append(connection)
        
    def stepNeuron(self):
        sum = 0
        for conn in range(len(self.myConnections)):
            sum += self.myConnections[conn] * self.connBias[conn]
        self.myOutput = 1 / (1 + math.e **( -self.myThreshold * sum ) )
    
    def trainNeuron(self, expectedOutput):
        pass
    
class tanhNeuron:
    def __init__(self, connectedNeurons):
        self.myConnectedNeurons = connectedNeurons
        self.connBias = [self.getRand() for I in range(len(self.myConnectedNeurons))]
        self.myOutput = 1
    
    def getRand(self):
        mu = 0
        sigma = .3
        return random.gauss(mu, sigma)
    
    def addConnection(self, connection):
        self.myConnections.append(connection)
        
    def stepNeuron(self):
        sum = 0
        for conn in range(len(self.myConnections)):
            sum += self.myConnections[conn] * self.connBias[conn]
        self.myOutput = (1 - math.e ** (-sum))/(1 + math.e ** (-sum))
    
    def trainNeuron(self, expectedOutput):
        pass

if __name__ == "__init__":
    self.input = 1
    myNeuron = self.tanhNeuron([self.input])
    