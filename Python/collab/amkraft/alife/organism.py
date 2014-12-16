import random

class Organism:
    def __init__(self, x, y, startingEnergy=100.0):
        self.x = x
        self.y = y
        self.energy = startingEnergy
        #self.energyBaselinePerStep = 1
        #self.energyCostPerMove = 1
        
        #self.neighborCellStates = [None for i in range(8)]
    
    def __str__(self):
        return 'B'
    
    def stepState(self):
        #request world info
        #
        #Calculate move
        #returns it's move
            #delta x and y

        x = random.randint(-1,1)
        y = random.randint(-1,1)
        return [x,y]
    