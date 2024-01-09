from api.modbus import Modbus
from api.utils import FunctionCode
from struct import pack, unpack


modbus = Modbus("127.0.0.1", 502)
modbus.connect()

modbus.functions.write_multiple_coils(11, 10,5,[
    True,
    True,
    True,
    True,
    True
])