#!/usr/bin/env  python

# This is the client side and uses TCP Sockets.
# This is not safe encryption!
# -*- coding: utf-8 -*-

import socket
import signal
import os
import sys
from Crypto.Cipher import AES

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    print("\n[*] Okay, quitting")
    sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)

def do_encrypt(message):
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
    message = pad(message)
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(message)
    return ciphertext

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)

    os.system('clear')
    target_host = "localhost"
    target_port = 9999

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host,target_port))
    print "[*] CLIENT STARTED"
    print "[*] Connected to %s:%d" % (target_host,target_port)
    print "[*] <Ctrl-C> to exit."
    print "[*] Type something in then hit <enter>:"
    PAYLOAD = raw_input()
    # send some data
    CRYP = do_encrypt(PAYLOAD)
    client.send(CRYP)

    # receive some data
    response = client.recv(4096)
    print response