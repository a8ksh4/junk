#!/usr/bin/env python

FRUITS = ['LIME', 'watermelon', 'Mango', 'KIWI', 'apricot', 'LEMON', 'fig', 'guava', 'Apple' ]

def main():
    # sort by name, case-insensitively
    ifruits = sorted(FRUITS, key=lambda e: e.lower())
    print " ".join(ifruits)

    # sort by length
    lfruits = sorted(FRUITS, key=lambda e: len(e))
    print " ".join(lfruits)

    # sort first by length, then by name, case-insensitively
    lifruits = sorted(FRUITS, key=lambda e: (len(e), e.lower()))
    print " ".join(lifruits)

if __name__ == '__main__':
    main()