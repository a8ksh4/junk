#!/usr/bin/env python

import socket
import pickle

class crypto:
    def __init__():
        pass

    def encrypt():
        pass
    
    def decrypt():
        pass

class Client():
    def __init__(self):
        HOST = 'localhost'    # The remote host
        PORT = 50006              # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

    def send(self):
        data = (1, (2, 2))
        s.send(pickle.dumps(data))
        pickledData = s.recv(1024)
        s.close()
        print 'Received', repr(pickle.loads(pickledData))

class Server():
    def __init__(self):
        HOST = ''                 # Symbolic name meaning the local host
        PORT = 50006              # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        print 'Connected by', addr

    def receive(self):
        while 1:
            pickledData = conn.recv(1024)
            if not pickledData: break
            data = pickle.loads(pickledData)
            print "Received: " + str(data)
            conn.send(pickle.dumps(data))
        conn.close()

