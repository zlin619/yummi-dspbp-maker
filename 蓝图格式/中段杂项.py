import struct
from dataclasses import dataclass

from 蓝图格式 import 类型
from 蓝图格式.坐标 import Int32平面坐标
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类


@dataclass
class 中段杂项(蓝图dataclass基类):
    # 一般为1
    版本: 类型.Int32
    补丁: 类型.Int32
    光标锚点偏移坐标: Int32平面坐标
    # 一般为0
    光标对应区域: 类型.Int32
    # 长按鼠标拖拽复制建筑时，间隔的长宽, 一般与areas.size相同
    拖拽框大小: Int32平面坐标
    # 一般为0
    主区域索引: 类型.Int32

    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转比特流(self) -> bytes:
        return struct.pack(
            '<7i',  # <表示小端序，7i表示7个32位整数
            self.版本,
            self.光标锚点偏移坐标.东西X,
            self.光标锚点偏移坐标.南北Y,
            self.光标对应区域,
            self.拖拽框大小.东西X,
            self.拖拽框大小.南北Y,
            self.主区域索引
        )
# 中段杂项 到此为止
