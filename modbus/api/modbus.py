from enum import Enum
import socket

from struct import pack, unpack

# https://en.wikipedia.org/wiki/Modbus#Public_function_codes

class FunctionCodes(Enum):
    ReadCoils = 1
    ReadDiscreteInputs = 2
    ReadMultipleHoldingRegisters = 3
    ReadInputRegisters = 4
    WriteSingleCoil = 5
    WriteSingleHoldingRegister = 6

    WriteMultipleCoils = 15
    WriteMultipleHoldingRegisters = 16

    ReadFileRecord = 20
    WriteFileRecord = 21
    MaskWriteRegister = 22
    ReadWriteMultipleHoldingRegisters = 23
    ReadFIFOQueue = 24

    ReadDeviceIdentification = 43

class Modbus:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send_bytes(self, bytes):
        self.socket.send(bytes)
        return self.socket.recv(1024)

    def unpack_bytes(self, bytes):
        return unpack("%sB" % len(bytes), bytes)