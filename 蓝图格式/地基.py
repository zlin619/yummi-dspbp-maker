import struct
from dataclasses import dataclass

import 蓝图格式.类型 as 类型
from 蓝图格式.地基矩形区域 import 地基矩形区域
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类


@dataclass
class 地基(蓝图dataclass基类):
    版本: 类型.UInt8
    矩形区域: list[地基矩形区域]
    地基调色盘掩码: 类型.UInt32
    地基调色盘: list[类型.UInt32]
    ########################
    # 以上为字段，以下为函数 #
    ########################

    def 转比特流(self) -> bytes:
        
        流数据 = bytearray()
        rectCount = len(self.矩形区域)
        流数据.extend(struct.pack("<B", self.版本))
        流数据.extend(struct.pack("<i", rectCount))
        for i in range(0,rectCount):
            流数据.extend(self.矩形区域[i].转比特流())
        
        colorCount = 0
        if self.地基调色盘掩码 != 0:
            colorCount = len(self.地基调色盘)
        
        流数据.extend(struct.pack("<Ii", self.地基调色盘掩码, colorCount))
        if colorCount == 0:
            return 流数据
        for i in range(0, colorCount):
            流数据.extend(struct.pack("<I", self.地基调色盘[i]))
        return 流数据
    # 转比特流 到此为止
# 地基 到此为止