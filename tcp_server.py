#!/usr/bin/env  python

# This is the server side and uses TCP Sockets.
# This is not encrypted!
# -*- coding: utf-8 -*-

import socket
import threading
import os

os.system('clear')
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
print "[*] SERVER STARTED"
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# this is our client-handling thread
def handle_client(client_socket):
    # print out what the client sends
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request
    # send back a packet
    client_socket.send("ACK!")
    client_socket.close()
while True:
    # Wait for a connection
    print "[*] Waiting for a connection."
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()