#!/usr/bin/python3           
# This is client.py file

import socket
import struct
import time
from struct import pack, unpack

# Create a TCP/IP socket
TCP_IP = 'localhost'
TCP_PORT = 502
BUFFER_SIZE = 39
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

try:

    unitId = 3
    functionCode = 5
    print("\n,Switching plug on")
    coilId = 1
    req = struct.pack('12B', 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, int(unitId), int(functionCode), 0x00, int(coilId),
                      0xff,
                      0x00)
    sock.send(req)
    print(unpack("%sB" % len(req), req))

    print(sock.recv(1024))

finally:
    print('\nCLOSING SOCKET')
    sock.close()