'''
Created on 2009-12-19

@author: drnorris
'''
import random, copy
                     
class GridThing:
    def __init__(self, gridSize=10, gridWrap=True, history=0):
        self.grid = [[False for col in range(gridSize)] for row in range(gridSize)]
        self.gridWrap = gridWrap
        self.gridSize = gridSize
        self.ruleList = [['Game of Life', [3], [2,3]], ['High Life', [3,6], [2,3]]]
        self.setEffectiveRule(0)
                
    def addRule(self, ruleName, birthValues, liveValues):
        self.ruleList.append([ruleName, [birthValues], [liveValues]])
    
    def getRules(self):
        return self.ruleList
    
    def getEffectiveRule(self):
        return self.effectiveRule
    
    def setEffectiveRule(self, ruleNumber):
        self.effectiveRule = ruleNumber
        self.birthValues = self.ruleList[ruleNumber][1]
        self.liveValues = self.ruleList[ruleNumber][2]
          
    def calcNextState(self, lastState, aliveNeighbors):
        if lastState == True:
            if not aliveNeighbors in self.liveValues:
                return False
            else:
                return True
        else:
            if aliveNeighbors in self.birthValues:
                return True
            else:
                return False

    def getState(self):
        return self.grid
    
    def printnice(self):
        for row in self.getState():
            print row
    
    def getSize(self):
        return self.gridSize
       
    def setState(self, row, col, cellState):
        self.grid[row][col] = cellState
   
    def clear(self):
        self.grid = [[False for col in range(self.gridSize)] for row in range(self.gridSize)]

    def randomize(self, seed=None):
        random.seed(seed)
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                self.grid[row][col] = bool(random.randint(0,1))

    
    def step(self):
        self.gridLastState = copy.deepcopy(self.grid)
        
        for row in range(self.gridSize):
            for col in range(self.gridSize): 
                aliveNeighbors = 0
                if self.gridLastState[row][col] == True:
                    aliveNeighbors -= 1
                for xOffset in [-1, 0, 1]:
                    for yOffset in [-1, 0, 1]:
                        checkXLoc = row + xOffset
                        checkYLoc = col + yOffset
                        if not -1 < (checkXLoc ) < self.gridSize or not -1 < ( checkYLoc ) < self.gridSize:
                            if self.gridWrap ==  False:
                                continue
                            else:
                                checkXLoc = checkXLoc % self.gridSize
                                checkYLoc = checkYLoc % self.gridSize
                             
                        if self.gridLastState[checkXLoc][checkYLoc] == True:
                            aliveNeighbors += 1
                self.grid[row][col] = self.calcNextState(self.gridLastState[row][col], aliveNeighbors)

        if self.grid == self.gridLastState:
            return False 
        else:
            return True
   

class PatternMaker:
    def __init__(self, gridObject):
        self.grid = gridObject

    def identifySymmetries(self):
        print "test"
        
    
    def fillRandomRandint(self):
        print "test"


                        
if __name__ == "__main__":
    mygrid = GridThing(3, True)
    mygrid.randomize(1)
    
    mygrid.printnice()
    mygrid.step()
    
    mygrid.printnice()
    

    mypm = PatternMaker(mygrid)
