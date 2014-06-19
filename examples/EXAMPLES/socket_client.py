#!/usr/bin/env python

import sys
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((socket.gethostname(),7777))

if len(sys.argv) > 1:
   msg = sys.argv[1]
else:
   msg = "default message"

s.sendall(msg)

reply = s.recv(4096)

print "Server said >",reply.strip(),"<"

s.close()
