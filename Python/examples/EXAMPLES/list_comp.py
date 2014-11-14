#!/usr/bin/env python

FRUITS = ['watermelon','apple','mango','kiwi','apricot','lemon','guava']

VALUES = [ 2, 42, 18, 92, "boom", ['a','b','c'] ]

def main():
    # make copy of FRUITS, applying upper() to each element
    ufruits = [ fruit.upper() for fruit in FRUITS ]

    # Select FRUITS that start with 'a'.
    # The expression is the element itself. No changes are needed
    afruits = [ fruit for fruit in FRUITS if fruit.startswith('a') ]

    # copy and multiply each value by 2
    doubles = [ v * 2 for v in VALUES ]


    print "ufruits:"," ".join(ufruits)
    print "afruits:"," ".join(afruits)
    print "doubles:",
    for d in doubles:
        print d,
    print

if __name__ == '__main__':
    main()