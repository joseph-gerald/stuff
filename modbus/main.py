from api.modbus import Modbus
from struct import pack, unpack


modbus = Modbus("127.0.0.1", 502)
modbus.connect()

"""
Request

This command is requesting the ON/OFF status of discrete coils # 20 to 56
from the slave device with address 17.
11 01 0013 0025 0E84

11: The Slave Address (11 hex = address17 )
01: The Function Code 1 (read Coil Status)
0013: The Data Address of the first coil to read.
             ( 0013 hex = 19 , + 1 offset = coil #20 )
0025: The total number of coils requested.  (25 hex = 37,  inputs 20 to 56 ) 
0E84: The CRC (cyclic redundancy check) for error checking.

Response

11 01 05 CD6BB20E1B 45E6

11: The Slave Address (11 hex = address17 )
01: The Function Code 1 (read Coil Status)
05: The number of data bytes to follow (37 Coils / 8 bits per byte = 5 bytes)
CD: Coils 27 - 20 (1100 1101)
6B: Coils 35 - 28 (0110 1011)
B2: Coils 43 - 36 (1011 0010)
0E: Coils 51 - 44 (0000 1110)
1B: 3 space holders & Coils 56 - 52 (0001 1011)
45E6: The CRC (cyclic redundancy check).
"""

# https://www.simplymodbus.ca/TCP.htm

byte_arr = [
    # MBAP HEADER

    0x00,    # Transaction Id
    0x00,    # Transaction Id
    0x00,    # Protocol Id
    0x00,    # Protocol Id
    0x00,    # Length
    0x6,    # Length
    int(11), # Unit Id

    # PDU

    int(5),  # Function Code
    0x00,
    0xAC,    # Coil Address
    0xFF,    # Status To Write
    0x00
]

bytes = pack(
    "%sB" % len(byte_arr),
    *byte_arr
)

response = modbus.send_bytes(bytes)
print("REQ: %s" % str(modbus.unpack_bytes(bytes)))

response = unpack("%sB" % len(response), response)
print("RES: %s" % str(response))