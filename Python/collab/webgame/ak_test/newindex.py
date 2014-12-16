from beaker.middleware import SessionMiddleware

def simple_app(environ, start_response):
    session = environ['beaker.session']

    if 'user_id' in session:
        logged_in = True
    else:
        logged_in = False
    
    session['user_id'] = 10

    start_response('200 OK', [('Content-type', 'text/plain')])
    
    out = "test"
    out += "\n"
    out += logged_in.__str__()

    #out += session['user_id']
    v = session['user_id'].__str__()
    if "user_id" in session:
        out += v
        
    session.save()
        
    return [out]

# Configure the SessionMiddleware
session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': True,
    }

application = SessionMiddleware(simple_app, session_opts)

