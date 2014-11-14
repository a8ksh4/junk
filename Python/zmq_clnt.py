#!/usr/bin/env python

import zmq

context = zmq.Context()

print "connecting to hello world server..."
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(1,10):
    print "Sending request: ", request, "..."
    socket.send("Hello")
    message = socket.recv()

    print "Received reply ", request, "[", message, "]"