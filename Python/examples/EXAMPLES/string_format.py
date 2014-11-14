#!/usr/bin/env python

from datetime import date

def main():
    basic_formatting()
    numeric_formatting()
    formatting_dates()
    selecting_from_a_list()
    selecting_from_a_dict()
    formatting_dates()
    formatting_objects()

def basic_formatting():
    color = 'blue'
    animal = 'iguana'

    print('{0} {1}'.format(color,animal))


def numeric_formatting():
    num = 13
    fahr = 98.6839832
    bignum = 4898349820234

    print('{0:.1f}'.format(fahr))
    print 'There are {0:04d} items'.format(num)
    print 'The answer is {0:,d}'.format(bignum)

def selecting_from_a_list():
    fruits = [ 'apple', 'mango', 'banana', 'cherry', 'watermelon', 'pineapple']

    print("{0[0]} {0[1]} {0[5]}".format(fruits))

def selecting_from_a_dict():

    airports = { 'IAD':'Dulles', 'YKF':'Waterloo International',
        'SEA':'Seattle-Tacoma' }

    print("from {0[IAD]} to {0[YKF]}".format(airports))


def formatting_dates():
    d = date(2012,1,1)

    print("{0.month} {0.day} {0.year}".format(d))
    print("{0.month:02d}/{0.day:02d}/{0.year:04d}".format(d))


def formatting_objects():
    class Movie(object):
        def __init__(self,title,director):
            self._title = title
            self._director = director

        @property
        def Title(self):
            return self._title

        @property
        def Director(self):
            return self._director

    movies = [
        Movie('Jaws','Spielberg'),
        Movie('Psycho','Hitchcock')
    ]

    for m in movies:
        print('{0.Title} by {0.Director}'.format(m))#!/usr/bin/env python

if __name__ == '__main__':
    main()