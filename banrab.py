#!/usr/bin/python3

import socket

"""
Banner grabber :D
"""

# Ask for the ip and port of the service to grab its banner
ip = input("[+] IP: ")

port = input("[+] Port: ")
port = int(port)

BUFF_SIZE = 4096 # Change if needed

# Grab time
s = socket.socket()
s.connect((ip, port))
banner = s.recv(BUFF_SIZE)

print(banner.decode('utf-8', errors='ignore'))
s.close()