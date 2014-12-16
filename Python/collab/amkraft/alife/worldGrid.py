import random
from organism import Organism
from food import Food

class WorldGrid:
    def reset(self):
        self.worldItems = []
        for i in range(10):
            self.placeRandomFood()
        for i in range(10):
            self.placeRandomOrganism()
        self.status = ""
        
    def __init__(self, gridSize=10, foodValue=100.0, movementCost=0.1, rand=random.Random()):
        self.gridSize = gridSize
        self.rand = rand
        self.foodValue = foodValue
        self.movementCost = movementCost
        self.reset()
        
    def moveBugs(self):
        for item in self.worldItems:
            if isinstance(item, Organism):
                moveDelta = item.stepState()
                item.x = (item.x + moveDelta[0]) % self.gridSize
                item.y = (item.y + moveDelta[1]) % self.gridSize
    
    def eatFood(self):
        foodEaten = 0
        for food in self.worldItems:
            if isinstance(food, Food):
                items = self.getItems(food.x, food.y)
                for bug in items:
                    if isinstance(bug, Organism):
                        if self.worldItems.count(food) > 0:
                            self.worldItems.remove(food)
                            bug.energy += self.foodValue
                            foodEaten += 1
        return foodEaten
                        
    def bugUseEnergy(self):
        for bug in self.worldItems:
            if isinstance(bug, Organism):
                bug.energy -= self.movementCost
                if bug.energy <= 0:
                    self.worldItems.remove(bug)
                    
    def replaceFood(self):
        food = self.getItemsOfType(Food)
        if len(food) < 10:
            for i in range(10 - len(food)):
                self.placeRandomFood()
                
    def mate(self):
        bugs = self.getItemsOfType(Organism)
        for m in bugs:
            for f in bugs:
                if m != f and m.x == f.x and m.y == f.y and m.energy >= 200 and f.energy >= 200:
                    m.energy -= 100
                    f.energy -= 100
                    self.worldItems.append(Organism(f.x, f.y))
    
    def updateStatus(self):
        self.status = "bugs = %d" % len(self.getItemsOfType(Organism))
   
    def stepGrid(self):
        self.moveBugs()
        foodEaten = self.eatFood()
        if(foodEaten):
            self.replaceFood()
            #self.placeRandomFood()
        
        self.mate()
        self.bugUseEnergy()
        self.updateStatus()
    
    def placeRandomOrganism(self):
        x = self.rand.randint(0,self.gridSize-1)
        y = self.rand.randint(0,self.gridSize-1)
        organism = Organism(x, y)
        self.worldItems.append(organism)
        
    def placeRandomFood(self):
        x = self.rand.randint(0,self.gridSize-1)
        y = self.rand.randint(0,self.gridSize-1)
        empty = True
        for cx in range(-1, 2):
            for cy in range(-1, 2):
                if len(self.getItems(x+cx,y+cy)) > 0:
                   empty = False
        if empty:
            self.worldItems.append(Food(x, y))

    def getItemsOfType(self, type):
        items = []
        for item in self.worldItems:
            if isinstance(item, type):
                items.append(item)
        return items
    
    def countItemsOfType(self, type):
        count = 0
        for item in self.worldItems:
            if isinstance(item, type):
                count += 1
        return count

    def getItems(self, x, y):
        x = x % self.gridSize
        y = y % self.gridSize
        
        items = []
        for item in self.worldItems:
            if item.x == x and item.y == y:
                items.append(item)
        return items

    def printGrid(self):
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                items = self.getItems(row, col)
                if len(items) < 1:
                    print '-',
                else:
                    print items[0],
            print
        print

if __name__ == '__main__':
    myWorld = WorldGrid()
    myWorld.printGrid()
    myWorld.stepGrid()
    myWorld.printGrid()
