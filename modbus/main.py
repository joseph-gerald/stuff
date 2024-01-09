from api.modbus import Modbus
from api.generators import FunctionCode
from struct import pack, unpack


modbus = Modbus("127.0.0.1", 502)
modbus.connect()

response = modbus.pass_function(FunctionCode.WriteSingleCoil, address=3, coil_address=5, status=True)

response = unpack("%sB" % len(response), response)
print("RES: %s" % str(response))