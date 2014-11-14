#!/usr/bin/env python

import socket

from president import President

def handle_client(client):
    
    while True:
        raw_request = client.recv(1024)
        
        if not raw_request:
            break
        
        (num,field) = raw_request.split() 
        
        p = President(num)
        
        
        if (field == 'FNAME'): response = p.FirstName
        if (field == 'LNAME'): response = p.LastName
        if (field == 'BDATE'): response = p.BirthDay
        if (field == 'DDATE'): response = p.DeathDay
        if (field == 'TSDATE'): response = p.TermStart
        if (field == 'TEDATE'): response = p.TermEnd
        if (field == 'PARTY'): response = p.Party
        if (field == 'BSTATE'): response = p.BirthState
        if (field == 'BPLACE'): response = p.BirthPlace
        
        client.send(response + '\n')

    client.close()
    
    return

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind( ('localhost',7777) )

server.listen(5)

while True:
        (c,addr) = server.accept()
        handle_client(c)

server.close()