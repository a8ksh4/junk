#!/usr/bin/env python
import MySQLdb
import json
from cgi import parse_qs, escape
from beaker.middleware import SessionMiddleware

def getdata(user = "unspecified"):
	db = MySQLdb.connect('localhost', 'root', 'R1ven', 'Web_game')
	cur = db.cursor()
	#cur.execute("SELECT ID, Name, Email FROM Players")
	cur.execute("show tables")
	
	return {'user': user, 'data': cur.fetchall()}

def application(environ, start_response):
	
	parameters = parse_qs(environ.get('QUERY_STRING', ''))
	#from beaker.middleware import SessionMidenviron['wsgi.input'].read()
	if 'user' in parameters:
		user = escape(parameters['user'][0])
	else:
		user = "unknown"

	output = json.dumps(getdata(user))
	start_response('200 OK', [('Content-type', 'text/plain')])
	return [output]

def main():
	print json.dumps(getdata())

if __name__ == "__main__":
	main()
