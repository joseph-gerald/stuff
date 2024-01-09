from api.modbus import Modbus
from api.utils import FunctionCode
from struct import pack, unpack


modbus = Modbus("127.0.0.1", 502)
modbus.connect()


print("Writing to coil on Slave #11 to True")
response = modbus.functions.write_single_coil(11, 5, True)
print("RES: %s" % str(response.data))

print("Reading coils from Slave #11 from index 4 -> 24 (4 + 20)")
response = modbus.functions.read_coils(11, 3, 20)
print("RES: %s" % str(response.data))

print("Reading input registers from Slave #12 form index 4 -> 25 (4 + 21)")
response = modbus.functions.read_input_registers(12, 4, 21)
print("RES: %s" % str(response.data))
