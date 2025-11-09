import struct
from dataclasses import dataclass

import 蓝图格式.类型 as 类型
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类

@dataclass
class 地基矩形区域(蓝图dataclass基类):
    版本: 类型.UInt8
    x: 类型.Int16
    y: 类型.Int16
    宽: 类型.UInt8
    高: 类型.UInt8
    地基数据: 类型.UInt8    # 装饰类型 | 调色盘id
    区域序号: 类型.UInt8    # 指回归线子区域在蓝图区域数据中的序号
    
    ########################
    # 以上为字段，以下为函数 #
    ########################

    def 转比特流(self) -> bytes:
        流数据 = bytearray()
        流数据.extend(struct.pack("<B", self.版本))
        流数据.extend(struct.pack(
            "<hh4B",
            self.x,
            self.y,
            self.宽,
            self.高,
            self.地基数据,
            self.区域序号
        ))
        return 流数据
    # 转比特流 到此为止
# 地基矩形区域 到此为止
