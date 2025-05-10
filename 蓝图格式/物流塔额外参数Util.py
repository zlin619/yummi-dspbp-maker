# from typing import Optional
# from typing import Type
from dataclasses import dataclass
from enum import IntEnum

import 蓝图格式.类型 as 类型
from 蓝图格式.图标 import 图标
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类

# 塔
class 运输模式(IntEnum):
    存储 = 0
    供应 = 1
    需求 = 2

class 沙盒锁定模式(IntEnum):
    不设置 = 0
    满仓 = 1
    一半 = 2
    空仓 = 3

class 带进出塔(IntEnum):
    不设置 = 0
    进塔 = 1
    出塔 = 2

class 集装层数(IntEnum):
    最大 = 0
    集装1层 = 1
    集装2层 = 2
    集装3层 = 3
    集装4层 = 4

@dataclass
class 物流塔格子(蓝图dataclass基类):
    物品ID: 图标
    本地运输模式: 运输模式
    星际运输模式: 运输模式
    存储上限: 类型.Int32
    锁定模式: 沙盒锁定模式

    @classmethod
    def 由数组构造(cls, p):
        return cls(图标(p[0]), 运输模式(p[1]), 运输模式(p[2]), p[3], 沙盒锁定模式(p[4]))

    def 转二进制数组(self):
        return [
            self.物品ID.序号,
            self.本地运输模式.value,
            self.星际运输模式.value,
            self.存储上限,
            self.锁定模式.value,
            0,
        ]

@dataclass
class 带子出口(蓝图dataclass基类):
    朝向: 带进出塔
    物品栏索引: 类型.Int32 # 对应第几个物品栏

    @classmethod
    def 由数组构造(cls, p):
        return cls(带进出塔(p[0]), 类型.Int32(p[1]))

    def 转二进制数组(self):
        return [
            self.朝向.value,
            self.物品栏索引,
            0,
            0,
        ]


