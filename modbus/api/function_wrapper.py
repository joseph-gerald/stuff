from .parsers import *
from .utils import *

class Functions:
    def __init__(self, modbus):
        self.modbus = modbus

    def read_coils(self, address: int, start: int, size: int) -> GenericBinaryRead:
        return GenericBinaryRead(self.modbus.pass_function(FunctionCode.ReadCoils, address=address, start=start, size=size), size)

    def read_discrete_inputs(self, address: int, start: int, size: int) -> GenericBinaryRead:
        return GenericBinaryRead(self.modbus.pass_function(FunctionCode.ReadDiscreteInputs, address=address, start=start, size=size), size)
    
    def read_multiple_holding_registers(self, address: int, start: int, size: int) -> GenericByteRead:
        return GenericByteRead(self.modbus.pass_function(FunctionCode.ReadMultipleHoldingRegisters, address=address, start=start, size=size), size)

    def read_input_registers(self, address: int, start: int, size: int) -> GenericByteRead:
        return GenericByteRead(self.modbus.pass_function(FunctionCode.ReadInputRegisters, address=address, start=start, size=size), size)

    def write_single_coil(self, address: int, coil_address: int, status: bool):
        return (self.modbus.pass_function(FunctionCode.WriteSingleCoil, address=address, coil_address=coil_address, status=status))

