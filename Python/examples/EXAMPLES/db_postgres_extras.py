#!/usr/bin/env python

import sys
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
   host="localhost",
   dbname="jstrick",
   user="scripts",
   password='scripts',
)

c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

c.execute('''
    select * from presidents where num = %s
''', (26,))

row = c.fetchone()
print row['fname'], row['lname']

print '{0[fname]} {0[lname]} is a {0[party]}'.format(row)