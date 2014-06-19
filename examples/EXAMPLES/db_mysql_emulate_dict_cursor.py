#!/usr/bin/env python

import MySQLdb

myconn = MySQLdb.connect(
   host="localhost",
   db="python2",
   user="scripts",
   passwd="scripts",
)

c = myconn.cursor()

def row_as_dict(cursor):
    '''Generate rows as dictionaries'''
    column_names = [desc[0] for desc in cursor.description]
    for row in cursor.fetchall():
        row_dict = dict(zip(column_names, row))
        yield row_dict
        

# select first name, last name from all presidents
num_recs = c.execute('''
    select lname, fname
    from presidents
''')

for row in row_as_dict(c):
    print row['fname'], row['lname']
    
