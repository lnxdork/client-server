#!/usr/bin/env  python

# This is the client side and uses UNIX Sockets, NOT TCP!
# This is not encrypted!
# -*- coding: utf-8 -*-

import socket
import os

os.system('clear')

NAME = "/tmp/.X11-font.lock"

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

if os.path.exists(NAME):
  client = socket.socket( socket.AF_UNIX, socket.SOCK_STREAM )
  client.connect(NAME)

  print "[*] CLIENT STARTED"
  print "[*] Type something in then hit <enter>:"
  PAYLOAD = raw_input()
  client.send(PAYLOAD)
  resp = client.recv(1024)
  print 'Received: "%s"' % resp
  client.close()

else:
	print "Couldn't Connect!"
