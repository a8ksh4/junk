#!/usr/bin/env python

import sqlite3

def fetch_iter(cursor,chunk_size):
    """ Fetch chunk_size records, but parcel them out one at a time """
    while True:
        rows = cursor.fetchmany(chunk_size)
        if not rows: # no more recs
            break
        for row in rows:
            yield row

with sqlite3.connect("../DATA/PRESIDENTS") as s3conn:
    s3cursor = s3conn.cursor()

    s3cursor.execute('select fname, lname from presidents')
    for row in fetch_iter(s3cursor, 10):  # in real life, a large number, such as 10000
        print ' '.join(row)
