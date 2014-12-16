#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
#import sys
def index():



	con = MySQLdb.connect('localhost', 'root', 
			'R1ven', 'Web_game')
	cur = con.cursor()
	
	cur.execute("SELECT * FROM Players")
	rows = cur.fetchall()
	s= ""
	for row in rows:
		s += row.__str__()
	con.close()
	return s
