#!/usr/bin/env python

import sqlite3

s3conn = sqlite3.connect("../DATA/PRESIDENTS")
# uncomment to make _all_ cursors dictionary cursors
# conn.row_factory = sqlite3.Row

NAME_QUERY = '''
    select lname, fname
    from presidents
    where num < 5
'''

cur = s3conn.cursor() 

# select first name, last name from all presidents
cur.execute(NAME_QUERY)

for row in cur.fetchall():
    print row
print '-' * 50

dcur = s3conn.cursor()

# make _this_ cursor a dictionary cursor
dcur.row_factory = sqlite3.Row

# select first name, last name from all presidents
dcur.execute(NAME_QUERY)

for row in dcur.fetchall():
    print row['fname'], row['lname']

print '-' * 50

# make cursors return str rather than unicode
s3conn.text_factory = str
tcur = s3conn.cursor()
tcur.execute(NAME_QUERY)
for row in tcur.fetchall():
    print row
