import socket

from .generators import *
from .utils import *
from .function_wrapper import Functions

from struct import pack, unpack

GENERATORS = [
    read_coils,
    read_discrete_inputs,
    read_multiple_holding_registers,
    read_input_registers,
    write_single_coil,
]

class Modbus:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.functions = Functions(self)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        HEADER = generate_mbap_header(len(DATA))

        # Combine header with data for final payload
        PAYLOAD = [*HEADER, *DATA]

        return self.send_bytes(self.pack_bytes(PAYLOAD))
