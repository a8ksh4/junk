#!/usr/bin/env python

import sys
import os
import sqlite3

myconn = sqlite3.connect("../DATA/PRESIDENTS")

with open('mkpres.sql') as MKPRES:
    sql_to_build_db = MKPRES.read()

cu = myconn.cursor()

table_check_sql = """
    select count(*)
    from sqlite_master
    where
        type = 'table'
        and
        name = 'presidents'
"""
cu.execute(table_check_sql)
result = cu.fetchone()
if result[0] > 0:
    cu.execute("drop table presidents")

cu.executescript(sql_to_build_db)

for row in cu.fetchall():
    print row
    
    
myconn.commit()
cu.close()
myconn.close()
