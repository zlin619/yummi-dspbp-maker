import struct

def int转struct转float(int_value: int) -> float:
    """将 int 的二进制数据解释为 float (IEEE 754)"""
    return struct.unpack('f', struct.pack('I', int_value))[0]

def float转struct转int(float_value: float) -> int:
    """将 float 的二进制数据存储为 int (IEEE 754)"""
    return struct.unpack('I', struct.pack('f', float_value))[0]
