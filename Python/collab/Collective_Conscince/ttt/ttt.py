import random

class nn:
    r = random.Random()
    weights = [r.random() *2.0-1.0 for i in range(9)]
    biases = [r.random() *2.0-1.0 for i in range(9)]
    
    def proc_inpt(self, input):
        output = [None for i in range(9)]
        for i in range(9):
            output[i] = input[i] * self.weights[i] + self.biases[i]

        return output
    
n = nn()
print n.weights
print n.biases

boardinput = [-1, -1, 0, 1, 1, 0, -1, -1, 0]
print boardinput

print n.proc_inpt(boardinput)
