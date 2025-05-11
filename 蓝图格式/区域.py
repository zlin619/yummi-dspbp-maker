import struct
from dataclasses import dataclass

import 蓝图格式.坐标 as 坐标
import 蓝图格式.类型 as 类型
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类


@dataclass
class 区域(蓝图dataclass基类):
    区域序号: 类型.Int8
    父区域序号: 类型.Int8
    tropic_anchor: 类型.Int16
    area_segments: 类型.Int16
    锚点偏移: 坐标.Int16平面坐标
    大小: 坐标.Int16平面坐标

    ########################
    # 以上为字段，以下为函数 #
    ########################
    def __hash__(self):
        return hash(self.区域序号)

    def 转比特流(self) -> bytes:
        return struct.pack(
            "<bbhhhhhh",
            self.区域序号,
            self.父区域序号,
            self.tropic_anchor,
            self.area_segments,
            self.锚点偏移.东西X,
            self.锚点偏移.南北Y,
            self.大小.东西X,
            self.大小.南北Y
        )
    # 转比特流 到此为止
# 区域 到此为止
