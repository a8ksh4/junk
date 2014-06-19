#!/usr/bin/env python
from datetime import date

pres_lname = raw_input("Enter president's last name: ")

with open("../DATA/presidents.txt") as pres_file:
    
    for rec in pres_file:
        fields = rec.split(":")
        if fields[1] == pres_lname:
            name = fields[2] + ' ' + fields[1]

            birth_date = date( int(fields[3]), int(fields[4]), int(fields[5]) )
            extra = ''

            try:
                death_date = date( int(fields[6]), int(fields[7]), int(fields[8]) )
            except ValueError as err:
                death_date = date.today()
                extra = '**'

            elapsed_time = death_date - birth_date
            age = elapsed_time.days/365

            print "{0:25s} {1}".format( name, age )

