#!/usr/bin/env python

import os
import sys
try:
    from urlparse import parse_qsl
except:
    from cgi import parse_qsl

import oauth2 as oauth

class TwitterToken():
    def __init__(self, ck=None, cs=None):
        self.REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
        self.ACCESS_TOKEN_URL  = 'https://api.twitter.com/oauth/access_token'
        self.AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
        self.SIGNIN_URL        = 'https://api.twitter.com/oauth/authenticate'
        if not ck and not cs:
            self.consumer_key    = 'UnvyGbcn3VxkSwjgqfI7I4MNT'
            self.consumer_secret = 'g31AE5JTP9SHlhH8Cb3byawOH959RkEv8EljlZ0E9CDmkHsLQz'

        self.signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
        self.oauth_consumer = oauth.Consumer(key=self.consumer_key, 
                                        secret=self.consumer_secret)
        self.oauth_client = oauth.Client(self.oauth_consumer)
        self.resp, self.content = self.oauth_client.request(
                                        self.REQUEST_TOKEN_URL, 'GET')

        if self.resp['status'] != '200':
            print 'Invalid respond from Twitter requesting temp token: %s' \
                    % self.resp['status']
        else:
            self.request_token = dict(parse_qsl(self.content))

        self.url = "{0}?oauth_token={1}".format(self.AUTHORIZATION_URL,
                                        self.request_token['oauth_token'])

    def getToken(self, pincode):
        token = oauth.Token(self.request_token['oauth_token'], 
                            self.request_token['oauth_token_secret'])
        token.set_verifier(pincode)

        oauth_client = oauth.Client(self.oauth_consumer, token)
        resp, content = oauth_client.request(self.ACCESS_TOKEN_URL, 
                            method='POST',
                            body='oauth_callback=oob&oauth_verifier=%s' \
                                % pincode)
        access_token = dict(parse_qsl(content))
        if resp['status'] != '200':
            return((resp['status'], ))
        else:
            return(access_token['oauth_token'], 
                    access_token['oauth_token_secret'])

if __name__ == '__main__':
    tt = twitterToken()
    print "Please visit this Twitter page and retrieve the pincode so" +\
            " we may generate an access token:"
    print "{0}\n".format(tt.url)

    pincode = raw_input('Pincode? ')

    token = tt.getToken(pincode)
    if len(token) > 1:
        print 'Your Twitter Access Token key: %s' % token[0]
        print '          Access Token secret: %s' % token[1]
    else:
        print "The request for a token did not succeed: {0}".format(token)
        
