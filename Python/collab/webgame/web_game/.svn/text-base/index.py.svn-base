from cgi import parse_qs, escape
import MySQLdb

html = """
<html>
  <body>
     <form method="post" action="">
        <p>
           Username: <input type="text" name="username">
        </p>
        <input type="submit" value="Submit">
   </form>
   <p>
      Passed Username: %s<br>
   </p>
</body>
</html>
"""

def getuser(user):
   db = MySQLdb.connect('localhost', 'root', 'R1ven', 'Web_game')
   cur = db.cursor()
   cur.execute("SELECT ID, Name FROM Players WHERE Name = %s", user)
   data = cur.fetchone()
   if data:
      return data
   return None

def application(environ, start_response):
   try:
      request_body_size = int(environ.get('CONTENT_LENGTH', 0))
   except (ValueError):
      request_body_size = 0

   request_body = environ['wsgi.input'].read(request_body_size)
   d = parse_qs(request_body)
   username = d.get('username', [''])[0]
   username = escape(username)
   response_body = html % (username or None)
   response_body += "User = " + getuser(username).__str__()
   start_response('200 OK', [('Content-Type', 'text/html')])

   return [response_body]
