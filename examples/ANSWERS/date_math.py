#!/usr/bin/env python
import sys
import datetime

if len(sys.argv) < 3:
    print "Please enter a date in YYYY-MM-DD format and an integer"
    sys.exit(1)

(year,month,day) = sys.argv[1].split("-")
thedate = datetime.date(int(year),int(month),int(day))

day_delta = datetime.timedelta(int(sys.argv[2]))

new_date = thedate + day_delta

print new_date
