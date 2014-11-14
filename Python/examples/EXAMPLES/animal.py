#!/usr/bin/env python

class Animal(object): 
    _COUNT = 0 

    def __init__(self, species, name, sound): 
        self._species = species 
        self._name = name 
        self._sound = sound 
        Animal._COUNT += 1 

    def kill(self): 
        Animal._COUNT -= 1 

    @property 
    def Species(self): 
        return self._species 
    
    @property 
    def Name(self): 
        return self._name 

    @property
    def Sound(self):
        return self._sound

    @property
    def ID(self):
        return "I am the {0}, hear me {1}".format(self.Species, self.Sound)

    def MakeSound(self): 
        print(self.Sound) 

    @classmethod
    def ZooSize(cls): 
        return cls._COUNT 

if __name__ == "__main__": 
    leo = Animal("African lion", "Leo", "Roarrrrrrr") 
    garfield = Animal("house cat", "Garfield", "Meowwwww") 
    felix = Animal("cartoon cat", "Felix", "Meowwwww") 

    print leo.Name,"is a", leo.Species, "--", 
    leo.MakeSound()

    print garfield.Name,"is a",garfield.Species,"--", 
    garfield.MakeSound() 

    print felix.Name,"is a",felix.Species,"--", 
    felix.MakeSound()

    print "Zoo size is:", Animal.ZooSize()
    leo.kill()  # :-(
    print "Zoo size is:", Animal.ZooSize()
