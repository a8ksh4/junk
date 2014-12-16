import pylab
food = [10, 5, 30]
bugs = [5, 10, 25]
p1 = pylab.plot(food, '-gs', label='food')
pylab.plot(bugs, '-bo', label='bugs')
pylab.title('Population over time')
pylab.ylabel('Population Count')
pylab.xlabel('Ticks')
pylab.legend(loc=0)
pylab.show()