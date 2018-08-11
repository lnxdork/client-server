#!/usr/bin/env  python

# This is the client side and uses UNIX Sockets, NOT TCP!
# This is not encrypted!
# -*- coding: utf-8 -*-

import socket
import sys
import os

os.system('clear')
NAME = "/tmp/.X11-font.lock"
 
if os.path.exists(NAME):
  os.remove(NAME)
 
server = socket.socket( socket.AF_UNIX, socket.SOCK_STREAM )
server.bind(NAME)
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

print "[*] SERVER STARTED"
server.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, '[*] Waiting for a connection.'
    connection, address = server.accept()
    try:
      print >>sys.stderr, 'Connection from:', address

      # Receive the data in small chunks and retransmit it
      while True:
        resp = connection.recv( 1024 )
        print >>sys.stderr, 'Received: "%s"' % resp
        if resp:
          print >>sys.stderr, '[*] Sending data back to the client.'
          connection.send(resp)
        else:
          print >>sys.stderr, 'No more data from: ', address
          break

    finally:
      connection.close()

server.close()
os.remove(NAME)
