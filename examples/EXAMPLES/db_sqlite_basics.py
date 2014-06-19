#!/usr/bin/env python

import sqlite3

with sqlite3.connect("../DATA/PRESIDENTS") as s3conn:

    s3cursor = s3conn.cursor()

    # select first name, last name from all presidents
    s3cursor.execute('''
        select lname, fname
        from presidents
    ''')
    

    print "Sqlite3 does not provide a row count\n"
    
    for row in s3cursor.fetchmany(10):
        print ' '.join(row)
    # note -- Sqlite3 does not return the number of rows
    print


    party_query = '''
    select lname, fname
    from presidents
    where party = ?
    '''

    for party in 'Federalist', 'Whig':
        s3cursor.execute(party_query, (party,))
        print s3cursor.fetchall()
        print

