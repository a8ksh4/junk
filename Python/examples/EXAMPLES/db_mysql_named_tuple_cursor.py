#!/usr/bin/env python

from collections import namedtuple
import MySQLdb

myconn = MySQLdb.connect(
   host="localhost",
   db="python2",
   user="scripts",
   passwd="scripts",
)

c = myconn.cursor()

def NamedTupleCursor(cursor):
    '''Generate rows as dictionaries'''
    column_names = [desc[0] for desc in cursor.description]
    name_str = ' '.join(column_names)
    # "RowTuple" is an arbitrary name -- any name could be used here
    RowTuple = namedtuple('RowTuple',name_str)
    
    
    for row in cursor.fetchall():
        row_tuple = RowTuple(*row)
        yield row_tuple
        

# select first name, last name from all presidents
num_recs = c.execute('''
    select lname, fname
    from presidents
''')

for row in NamedTupleCursor(c):
    print row.fname, row.lname
    
