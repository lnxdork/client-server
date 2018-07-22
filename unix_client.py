#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import os
import sys

NAME = "/tmp/.X11-font.lock"

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

if os.path.exists(NAME):
  client = socket.socket( socket.AF_UNIX, socket.SOCK_STREAM )
  client.connect(NAME)

  print "[*] CLIENT STARTED"
  print >>sys.stderr, '[*] Type something in then hit <enter>:'
  PAYLOAD = raw_input()
  client.send(PAYLOAD)
  resp = client.recv(1024)
  print >>sys.stderr, 'Received: "%s"' % resp
  client.close()

else:
	print >> sys.stderr, "Couldn't Connect!"
