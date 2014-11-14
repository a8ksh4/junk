#!/usr/bin/env python

from datetime import datetime as DateTime, date as Date, time as Time, timedelta as TimeDelta


def main():
    todays_date()
    sep()
    current_time()
    sep()
    date_deltas()
    sep()


def sep():
    print '-' * 50


def todays_date():
    print "date.today():",Date.today()


def current_time():
    now = DateTime.now()
    print "now.day:", now.day
    print "now.month:", now.month
    print "now.year:", now.year
    print "now.hour:", now.hour
    print "now.minute:", now.minute
    print "now.second:", now.second


def date_deltas():
    d1 = DateTime(2013,6,13)
    d2 = DateTime(2013,8,24)

    d3 = d2 - d1

    print "raw time delta:",d3
    print "time delta days:",d3.days

    t1 = DateTime(2007,8,24,10,4,34)
    t2 = DateTime(2007,8,24,22,8,1)
    t3 = t2 - t1

    print "t1 = datetime(2007,8,24,10,4,34):",t1
    print "t2 = datetime(2007,8,24,22,8,1):",t2
    print "time diff (t2 - t1):",t3

if __name__ == '__main__':
    main()