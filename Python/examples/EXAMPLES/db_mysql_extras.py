#!/usr/bin/env python

import MySQLdb
import MySQLdb.cursors

myconn = MySQLdb.connect(
   host="localhost",
   db="python2",
   user="scripts",
   passwd="scripts",
   cursorclass = MySQLdb.cursors.DictCursor
)

# c = myconn.cursor(MySQLdb.cursors.DictCursor) 
c = myconn.cursor()

# select first name, last name from all presidents
num_recs = c.execute('''
    select lname, fname
    from presidents
''')

print c.description

for row in c.fetchall():
    print row['fname'], row['lname']
print

c.execute('''
    select * from presidents where num = %s
''', (16,))

row = c.fetchone()
print row
print '-' * 50

# call a stored proc

cur = myconn.cursor(MySQLdb.cursors.Cursor)

cur.execute('call pres_full_name(16)')
print cur.fetchone()
cur.close()

cur = myconn.cursor(MySQLdb.cursors.Cursor)
cur.callproc('pres_full_name', (16,))
print cur.fetchone()

