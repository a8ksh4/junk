#!/usr/bin/env python

import socket

for n in xrange(1,45):
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect( ('localhost',7777) )
    c.send(str(n) + ' LNAME\n')
    lname = c.recv(1024).strip()
    c.send(str(n) + ' FNAME\n')
    fname = c.recv(1024).strip()   
    c.send(str(n) + ' PARTY\n')
    party = c.recv(1024).strip()   
    c.close()
    
    print '{0:20.20} {1:10.10} ({2})'.format(fname, lname, party)