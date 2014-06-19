#!/usr/bin/env python

from random import choice
import sqlite3

candidate =  (
    'Nader', 'Ralph','Winstead', 'Connecticut', '1934-02-27','Independent'
)

conn = sqlite3.connect("../DATA/PRESIDENTS")

c = conn.cursor()

insert_stmt = '''
   INSERT INTO presidents
    (num, lname, fname, dstart, dend,
     birthplace, birthstate, dbirth, ddeath, party)
     VALUES
    (45, ?, ?, '2012-01-20', '2016-01-20',
     ?, ?, ?, NULL, ?);
'''

try:
    rows = c.execute(insert_stmt, candidate)
except StandardError as e:
    print "Error inserting record:", e
    conn.rollback()
else:
    print "Record inserted OK."
    conn.commit()
