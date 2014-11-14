#!/usr/bin/env python

def main():
    cr1 = color_repeat('red', 3)
    print cr1()  # does not need parameters

    cr2 = color_repeat('blue', 5)
    print cr2()

def color_repeat(color, n):
    def _tmp():
        return color * n   # remembers values of color and n

    return _tmp

if __name__ == '__main__':
    main()
