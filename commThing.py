#!/usr/bin/env python

import os
import sys
from twittertoken import TwitterToken

class TwitterThing():
    def __init__(self):
        self.configPath = os.path.expanduser('~/.twitter_oauth.commThing')
        self.consumer_key    = 'UnvyGbcn3VxkSwjgqfI7I4MNT'
        self.consumer_secret = 'g31AE5JTP9SHlhH8Cb3byawOH959RkEv8EljlZ0E9CDmkHsLQz'
        if not os.path.exists(self.configPath):
            self._setupUserToken()
        try:
            cf = open(self.configPath, 'r')
            self.user_key, self.user_secret = cf.readlines().split('\n')
            cf.close()
        except:
            print 'Failed at user token... rm {0} and try again.'.format(
                    self.configPath)
            sys.exit()

    def _setupUserToken(self):
        if os.path.exists(self.configPath):
            os.remove(self.configPath)
        tt = TwitterToken(self.consumer_key, self.consumer_secret)
        print "Please visit this Twitter page and retrieve the pincode so" +\
                " we may generate an access token:"
        print "{0}\n".format(tt.url)

        pincode = raw_input('Pincode? ')

        token = tt.getToken(pincode)
        if len(token) > 1:
            print 'Got Token!  Continuing...'
            cf = open(self.configPath, 'w')
            cf.write('{0}\n{1}'.format(token[0], token[1])
            cf.close()
        else:
            print "The request for a token did not succeed: {0}".format(token)
            sys.exit()

    def post(self, blah):
        pass

    def get(self, friends=None):
        pass

class ZmqThing():
    def __init__(self):
        pass
