import random
import math

def Main():
    inputs = [[ 0.72, 0.82 ], [ 0.91, -0.69 ], [ 0.46, 0.80 ],
        [ 0.03, 0.93 ], [ 0.12, 0.25 ], [ 0.96, 0.47 ],
        [ 0.79, -0.75 ], [ 0.46, 0.98 ], [ 0.66, 0.24 ],
        [ 0.72, -0.15 ], [ 0.35, 0.01 ], [ -0.16, 0.84 ],
        [ -0.04, 0.68 ], [ -0.11, 0.10 ], [ 0.31, -0.96 ],
        [ 0.00, -0.26 ], [ -0.43, -0.65 ], [ 0.57, -0.97 ],
        [ -0.47, -0.03 ], [ -0.72, -0.64 ], [ -0.57, 0.15 ],
        [ -0.25, -0.43 ], [ 0.47, -0.88 ], [ -0.12, -0.90 ],
        [ -0.58, 0.62 ], [ -0.48, 0.05 ], [ -0.79, -0.92 ],
        [ -0.42, -0.09 ], [ -0.76, 0.65 ], [ -0.77, -0.76 ]]

    outputs = [  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    patternCount = len(inputs)
    
    r = random.Random()
    weights = [ r.random(), r.random() ]
    learningRate = 0.1
    iteration = 0
    globalError = -1
    
    while globalError != 0:
        globalError = 0
        for p in range(patternCount):
            output = Output(weights, inputs[p][0], inputs[p][1])
            localError = outputs[p] - output
            if localError != 0:
                for i in range(2):
                    weights[i] += learningRate * localError * inputs[p][i]
            globalError += math.fabs(localError)
        
        print("Iteration %f\tError %f" % (iteration, globalError))
        iteration += 1
    
    print("")
    print("X, Y, Output")
 
    x = -1.0
    while x <= 1.0:
        y = -1.0
        while y <= 1.0:
            output = Output(weights, x, y)
            if(output == 1):
                color = "Blue"
            else:
                color = "Red"
            print("%f, %f, %s" % (x, y, color))
            y += 0.5
        x += 0.5

def Output(weights, x, y):
    sum = x * weights[0] + y * weights[1]
    if sum >= 0:
        return 1
    return -1

Main()
