#!/usr/bin/env python

import socket
import pickle

HOST = ''                 # Symbolic name meaning the local host
PORT = 50006              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    pickledData = conn.recv(1024)
    if not pickledData: break
    data = pickle.loads(pickledData)
    print "Received: " + str(data)
    conn.send(pickle.dumps(data))
conn.close()

