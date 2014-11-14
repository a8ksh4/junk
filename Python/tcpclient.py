#!/usr/bin/env python

import socket
import pickle

HOST = 'localhost'    # The remote host
PORT = 50006              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = (1, (2, 2))
s.send(pickle.dumps(data))
pickledData = s.recv(1024)
s.close()
print 'Received', repr(pickle.loads(pickledData))

