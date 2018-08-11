#!/usr/bin/env  python

# This is the client side and uses TCP Sockets.
# This is not encrypted!
# -*- coding: utf-8 -*-

import socket
import os

os.system('clear')
target_host = "localhost"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))
print "[*] CLIENT STARTED"
print "[*] Type something in then hit <enter>:"
PAYLOAD = raw_input()
# send some data
client.send(PAYLOAD)

# receive some data
response = client.recv(4096)
print response