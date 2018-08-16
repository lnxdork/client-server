#!/usr/bin/env  python

# This is the server side and uses TCP Sockets.
# This is not safe encryption!
# It will accept any connection.
# It expects text in mod16.
# -*- coding: utf-8 -*-

import socket
import threading
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

def do_decrypt(ciphertext):
    BS = 16
    unpad = lambda s : s[:-ord(s[len(s)-1:])]
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    message = obj.decrypt(ciphertext)
    return unpad(message)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)

    os.system('clear')
    bind_ip = "0.0.0.0"
    bind_port = 9999
    
    if len(sys.argv) >= 2:
        bind_ip = sys.argv[1]
        bind_port = int(sys.argv[2])

    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    print "[*] SERVER STARTED"
    server.listen(5)
    print "[*] Listening on %s:%d" % (bind_ip,bind_port)
    print "[*] <Ctrl-C> to exit."

    # this is our client-handling thread
    def handle_client(client_socket):
        # print out what the client sends
        request = client_socket.recv(4096)
        print "[*] Received RAW: %s" % request
        DCRY = do_decrypt(request)
        print "[*] Received: %s" % DCRY    
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