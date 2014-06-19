#!/usr/bin/env python

import sys
import datetime

if len(sys.argv) < 3:
    print "Please enter two dates in format YYYY-MM-DD"
    sys.exit(1)

(year,month,day) = sys.argv[1].split("-")
date1 = datetime.date(int(year),int(month),int(day))

(year,month,day) = sys.argv[2].split("-")
date2 = datetime.date(int(year),int(month),int(day))

elapsed =  date2 - date1

# divmod returns (elapsed.days/365, elapsed.days % 365)
num_years, num_days = divmod(elapsed.days, 365)

print "{0:.0f} years {1:.0f} day(s)".format(num_years, num_days)
