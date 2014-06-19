#!/usr/bin/env python
from datetime import datetime, date

info = []
with open('../DATA/presidents.txt') as PRES:
    for line in PRES:
        (
             term_num,lname,fname,
             byear,bmon,bday,dyear,dmon,dday,
             bplace,bstate,
             tsyear,tsmon,tsday,teyear,temon,teday,
             party
        )  = line[:-1].split(':')
        
        name = '%s %s' % (fname,lname)
        
        if dyear:
            death_datetime = datetime.strptime(dyear+dmon+dday,'%Y%m%d')
            death_date = datetime.date(death_datetime)
        else:
            death_date = date.today()
                      
        info.append( (name,death_date,party  ) )

for p in sorted(info,key=lambda e: e[1]):
    print "{0:35s} {1} {2}".format(*p)
