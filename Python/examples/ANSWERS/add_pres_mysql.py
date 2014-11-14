#!/usr/bin/env python

from random import choice
import MySQLdb

candidate =  (
    'Nader', 'Ralph','Winstead', 'Connecticut', '1934-02-27','Independent'
)

myconn = MySQLdb.connect(
   host="localhost",
   db="python2",
   user="python2",
   passwd="python2"
);

c = myconn.cursor()

insert_stmt = '''
   INSERT INTO presidents
    (num, lname, fname, dstart, dend,
     birthplace, birthstate, dbirth, ddeath, party)
     VALUES
    (45, %s, %s, '2012-01-20', '2016-01-20',
     %s, %s, %s, NULL, %s);
'''

rows = c.execute(insert_stmt, candidate)

if rows == 1:
    print "Record inserted OK."
    myconn.commit()
else:
    print "Error inserting record:"
