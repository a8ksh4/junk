import sys; sys.path.append('../')
from web.wsgi import *

def simpleApp(environ, start_response):
    if not environ.has_key('web.auth.user'): # No user signed in
        start_response('403 User not signed in', [])
        return []
    elif not environ['web.auth.user'].authorise(app='app', level=1):
        start_response('403 The user does not have permission to access this application', [])
        return []
    else:
        start_response('200 OK', [('Content-type','text/html')])
        if environ['web.cgi'].has_key('mode') and environ['web.cgi']['mode'].value == 'signOut':
            environ['web.auth'].signOut()
            return ["""<html>
                <head><title>Auth Example</title></head>
                <body bgcolor="#ffffcc"><h1>Signed Out</h1><p><a href="auth">Sign in</a></p></body>
                </html>"""]
        else:
            return ["""<html>
                <head><title>Auth Example</title></head>
                <body bgcolor="#ffffcc"><h1>Congratulations!</h1>
                <p>Signed in!</p>
                <p><a href="auth?mode=signOut">Sign out</a>, <a href="auth">Visit again</a></p>
                </body></html>"""]

# Middleware Setup
application = error.Error(
    database.Database(
        session.Session(
            cgi.CGI(
                auth.Auth(
                    simpleApp, 
                    driver='database',
                    autoCreate=1,
                    expire=0,
                    idle=10,
                    template = """
                        <html>
                        <head><title>Auth Example</title></head>
                        <body bgcolor="#ffffcc">
                        <h1>Sign In</h1>
                        %(form)s
                        <p>%(message)s</p>
                        </body>
                        </html>
                    """,
                    redirectMethod='metaRefresh'
                ),
            ),
            expire = 1000,
            autoCreate = 1,
            driver='database',
        ),
        adapter = 'snakesql',
        database = 'wsgi-auth',
        autoCreate = 1
    ),
)
