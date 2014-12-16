#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys

def getdata():
	con = None
	mdb = MySQLdb
	
	con = mdb.connect('localhost', 'root', 'R1ven', 'Web_game')
	
	with con:
		cur = con.cursor()
		cur.execute("SELECT XLocation,Ylocation FROM SolarSystems")
	
		rows = cur.fetchall()
		
		return rows.__str__()


def application(environ, start_response):
        status = '200 OK'
        output = getdata()
        response_headers = [('Content-type', 'text/plain'),
                            ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        return [output]
