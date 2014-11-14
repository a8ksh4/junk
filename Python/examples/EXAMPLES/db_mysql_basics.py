#!/usr/bin/env python

import sys
import MySQLdb

# NOTE: MySQLdb.connect returns *cursor*, not *connection* under context manager
with MySQLdb.connect(
   host="localhost",
   db="python2",
   user="scripts",
   passwd="scripts"
) as mycursor:
    
    # select first name, last name from all presidents
    row_count = mycursor.execute('''
        select lname, fname
        from presidents
    ''')

    print "{0} rows in result set\n".format(row_count)
    
    for row in mycursor.fetchmany(10):
        print ' '.join(row)
    print
    
    party = 'Whig'
    
    mycursor.execute('''
    select lname, fname
    from presidents
    where party = %s
    ''', (party,))
    
    print mycursor.fetchall()

