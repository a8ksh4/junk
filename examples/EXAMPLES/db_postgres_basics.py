#!/usr/bin/env python

import sys
import psycopg2

pgconn = psycopg2.connect(
   host="localhost",
   dbname="jstrick",
   user="scripts",
   password='scripts',
)
pgcursor = pgconn.cursor() 

# select first name, last name from all presidents
pgcursor.execute('''
    select lname, fname
    from presidents
''')

print "{0} rows in result set\n".format(pgcursor.rowcount)

for row in pgcursor.fetchmany(10):
    print ' '.join(row)
print

party = 'Whig'

pgcursor.execute('''
select lname, fname
from presidents
where party = %s
''', (party,))

print pgcursor.fetchall()

pgconn.close()