'''
Created on 2010-01-01

@author: drnorris
'''

from multiprocessing import Process

class NameThing:
    def __init__(self):
        self.numThreads = 4
        self.threads = [None for i in range(self.numThreads)]
        for i in range(self.numThreads):
            self.threads[i] = Process(target=self.threadFunction, args=(i,))
    
    def start(self):
        for i in range(self.numThreads):
            self.threads[i].start()
            #self.threads[i].join()
    
    def printPIDs(self):
        for i in range(self.numThreads):
            print self.threads[i].pid

    def threadFunction(name):
        print 'I am ', name
    
if __name__ == '__main__':
    myNT = NameThing()
    myNT.printPIDs()
    myNT.start()