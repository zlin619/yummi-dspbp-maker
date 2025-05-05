import struct
from dataclasses import dataclass
from typing import Any

import 蓝图格式.坐标 as 坐标格式
import 蓝图格式.类型 as 类型
from 蓝图格式.图标 import 图标
from 蓝图格式.模型 import 模型
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类
from 蓝图格式.额外参数 import 额外参数

@dataclass
class 建筑主导接口(蓝图dataclass基类):
    目标序号: 类型.Int32 = -1
    目标接口: 类型.Int8 = -1
    自身接口: 类型.Int8 = -1
    插槽偏移: 类型.Int8 = 0
    # 晨隐说插槽偏移常见于分拣器, 但我不知道这玩意干嘛的


@dataclass
class 建筑(蓝图dataclass基类):
    建筑序号: 类型.Int32
    区域序号: 类型.Int8

    物品序号: 图标
    模型序号: 模型

    # 原版蓝图根据物品序号解析
    # 蓝图工具根据解析方式解析
    空间姿态: 坐标格式.姿态

    输出接口: 建筑主导接口
    输入接口: 建筑主导接口

    配方序号: 类型.UInt16  # 常见于制造厂类建筑
    过滤物品序号: 图标  # UInt16,常见于分拣器、四向
    额外参数: 额外参数

    # TODO:
    # 以下并非正式数据的一部分
    # 被动链接: Any = None
    # 玩家标注: Any = None

    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转比特流(self) -> bytes:
        流数据 = bytearray()
        流数据.extend(struct.pack("<i", -101))
        流数据.extend(
            struct.pack(
                "<iHHb",
                self.建筑序号,
                self.物品序号.转int(),
                self.模型序号.转int(),
                self.区域序号,
            )
        )
        流数据.extend(self.空间姿态.转比特流())
        流数据.extend(
            struct.pack(
                "<iiBBBBBBHH",
                self.输出接口.目标序号,
                self.输入接口.目标序号,
                self.输出接口.目标接口,
                self.输入接口.自身接口,
                self.输出接口.自身接口,
                self.输入接口.目标接口,
                self.输出接口.插槽偏移,
                self.输入接口.插槽偏移,
                self.配方序号,
                self.过滤物品序号.转int(),
            )
        )
        流数据.extend(self.额外参数.转比特流())
        return 流数据

    # 转比特流 到此为止


# 建筑 到此为止
