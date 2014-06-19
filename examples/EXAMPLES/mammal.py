#!/usr/bin/env python

from  animal import Animal 


class Mammal(Animal): 
    ''' 
        An animal that gives birth to live offspring 
        (as opposed to laying eggs). 
    ''' 
    def __init__(self, species, name, sound, gestation): 
        Animal.__init__(self, species, name, sound) 
        self._gestation = gestation 

    @property 
    def Gestation(self): 
        """Length of gestation period in days""" 
        return self._gestation 

if __name__ == "__main__": 
    m1 = Mammal("African lion", "Bob","Roarrrr",120)
    print m1.Name, "is a", m1.Species,"--",
    m1.MakeSound() 

    print "Number of animals", m1.ZooSize()

    m2 = Mammal("Fruit bat", "Freddie", "Squeak!!", 180) 
    print m2.Name, "is a", m2.Species, "--",
    m2.MakeSound() 

    print "Number of animals", m2.ZooSize()
    print "Number of animals", Mammal.ZooSize()

    m1.kill() 
    print "Number of animals", Mammal.ZooSize()

    print "Gestation period of the", m1.Species,"is",m1.Gestation,"days"
    print "Gestation period of the", m2.Species,"is",m2.Gestation,"days"
