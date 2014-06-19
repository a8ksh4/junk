#!/usr/bin/env python

import socket
import threading

class ClientHandler(threading.Thread):
    '''A thread to handle one client request'''
    
    def __init__(self, client_socket, client_address):
        super(ClientHandler, self).__init__()
        self._client_socket = client_socket
        self._client_address = client_address

    def run(self):
        request = self._client_socket.recv(1024)
        
        reply = request.upper()[::-1]  # upper & reversed
    
        self._client_socket.sendall(reply)
        self._client_socket.close()

def setup():
    '''Initialize the server socket'''
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # serv.setblocking(0)
    
    serv.bind((socket.gethostname(), 7777))
    
    serv.listen(5)
    
    return serv

def main():
    '''Main program.'''
    serv = setup()
    while True:
        (csock, addr) = serv.accept()
        handler = ClientHandler(csock, addr)
        handler.start()

       
if __name__ == '__main__':
    main()