from api.modbus import Modbus
from api.generators import FunctionCode
import unittest

modbus = Modbus("127.0.0.1", 502)

class TestModbus(unittest.TestCase):
    def test_connection(self):
        print("Establishing connection with Modbus...")
        modbus.connect()
        print("Sucesfully established connection!")

    def test_read_write_coils(self):
        print("\nWriting to coil #1 on Slave #11 to True")
        res = modbus.functions.write_single_coil(11, 0, True)

        print("\nWriting to coil #3 on Slave #11 to True")
        res = modbus.functions.write_single_coil(11, 2, True)

        print("\nWriting to coils #9, #10, #12 on Slave #11 to True")
        res = modbus.functions.write_multiple_coils(11, 8, 4, [
            True,
            True,
            False,
            True
        ])

        print("\nReading coils from Slave #11 from index 0 -> 20 (0 + 20)")
        print("Expecting for coils # 1, 3, 9, 10, 12 to be True")
        
        coil_data = modbus.functions.read_coils(11, 0, 16).data
        
        print("\nCoils:", coil_data)

        self.assertTrue(coil_data[0])
        self.assertTrue(coil_data[2])
        self.assertTrue(coil_data[8])
        self.assertTrue(coil_data[9])
        self.assertTrue(coil_data[11])

        print("Coils were as expected!")

    def test_read_input_registers(self):
        res = modbus.functions.read_input_registers(12, 4, 21)

        print("\nInput Registers:", res.data)
    
    def test_set_coils_to_zero(self):
        print("\nWriting to coils #0 -> #100 to False/OFF")
        res = modbus.functions.write_multiple_coils(11, 0, 100, [True]*100)
        




if __name__ == '__main__':
    unittest.main(exit=False)

