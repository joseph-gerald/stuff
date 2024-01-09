from api.modbus import Modbus
from api.generators import FunctionCode
import unittest

modbus = Modbus("127.0.0.1", 502)

class TestStringMethods(unittest.TestCase):

    def test_connection(self):
        modbus.connect()


    def test_read_coils(self):
        pass


if __name__ == '__main__':
    unittest.main(exit=False)

