#!/usr/bin/env python
import MySQLdb
import cgi
import sys
from cgi import parse_qs, escape

def showLogin():
	#return '<a href="?user=asdf">login</a>'
	out = """
<form action="?" method="POST">
  <input name="user" />
  <input name="submit" title="submit" id="submit" type="submit" />
</form>
"""
	return out

def loggedIn(user):
	out = """
Welcome {user}<br>\n
<a href="?">Logout</a>
"""
	return out.format(user=user)


def get_post_form(environ):
	assert is_post_request(environ)
	input = environ['wsgi.input']
	post_form = environ.get('wsgi.post_form')
	if (post_form is not None
	    and post_form[0] is input):
		return post_form[2]
	# This must be done to avoid a bug in cgi.FieldStorage
	environ.setdefault('QUERY_STRING', '')
	fs = cgi.FieldStorage(fp=input,
			      environ=environ,
			      keep_blank_values=1)
	new_input = InputProcessed('')
	post_form = (new_input, input, fs)
	environ['wsgi.post_form'] = post_form
	environ['wsgi.input'] = new_input
	return fs

class InputProcessed(object):
	def read(self, *args):
		raise EOFError('The wsgi.input stream has already been consumed')
	readline = readlines = __iter__ = read


def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/html')])

	parameters = parse_qs(environ.get('QUERY_STRING', ''))
	
	out = ""
	
	post = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=1)

	#return post.__str__()
	body = environ['wsgi.input']
	#return body
	#return post
	#post_form = get_post_form(environ)

	if 'user' in parameters:
		user = escape(parameters['user'][0])
	else:
		user = None
		
	if user == None:
		return showLogin()
	else:
		return loggedIn(user)
