import socket

from .generators import *
from .utils import *

from struct import pack, unpack

GENERATORS = [
    read_coils,
    read_discrete_inputs,
    read_multiple_holding_registers,
    read_input_registers,
    write_single_coil,
]


class Modbus:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __generateMBAPHeader(self, length, transaction_id=0, protcol_id=0):
        # https://www.simplymodbus.ca/TCP.htm

        mbap = [
            *bytify(transaction_id),  # Split transaction id into 2 bytes
            *bytify(protcol_id),  # Split protocol id into 2 bytes
            *bytify(length)  # Split length into 2 bytes
        ]

        return mbap

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send_bytes(self, bytes):
        self.socket.send(bytes)
        return self.socket.recv(1024)

    def unpack_bytes(self, bytes):
        return unpack("%sB" % len(bytes), bytes)

    def pack_bytes(self, bytes):
        # equivalent to latter given bytes is an array of 3 0s
        # pack(3B, 0, 0, 0)
        return pack("%sB" % len(bytes), *bytes)

    def pass_function(self, function_code: int, **kwargs):
        """
        pass_function(function_code, kwargs)

        Generate and send payload to modbus
        """

        DATA = GENERATORS[function_code.value - 1](kwargs)
        HEADER = self.__generateMBAPHeader(len(DATA))

        # Combine header with data for final payload
        PAYLOAD = [*HEADER, *DATA]
        print(PAYLOAD)

        return self.send_bytes(self.pack_bytes(PAYLOAD))
