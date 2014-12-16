import random

class board:
    def __init__(self):
        self.tackgrid = [[ None for col in range(3)] for row in range(3) ]
    
    def setcell(self, xaddress, yaddress, state):
        self.tackgrid[xaddress][yaddress] = state
        
    def printgrid(self):
        for row in range(3):
            print self.tackgrid[row]
        print ""
        
    def compmove(self):
        while True:
            xaddress = random.randint(0,2)
            yaddress = random.randint(0,2)
            if self.tackgrid[xaddress][yaddress] == None:
                self.tackgrid[xaddress][yaddress] = "O"
                break
            

def main():
    myboard = board()
    while True:
        xreply = int(raw_input('Please enter a row'))
        yreply = int(raw_input('Please enter a col'))
        myboard.setcell(xreply, yreply, "X")
        myboard.compmove()
        myboard.printgrid()
    
    
    
if __name__ == '__main__':
    main()
