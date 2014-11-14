#!/usr/bin/env python

import sys
import datetime

if len(sys.argv) < 2:
    print "Please enter a date in format YYYY-MM-DD"
    sys.exit(1)

(year,month,day) = sys.argv[1].split("-")

that_date = datetime.date(int(year),int(month),int(day))

elapsed = datetime.date.today() - that_date

years = elapsed.days/365
days = elapsed.days % 365
print "{0:.0f} years {1} days".format(years,days)
