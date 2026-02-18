# 全息信标额外参数：颜色、投影高度/半径、标记等级、信息等级、图标
from dataclasses import dataclass
from enum import IntEnum

from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类


class 标记等级(IntEnum):
    离线 = 0
    视野范围内 = 1
    本地星球 = 2
    本地星系 = 3
    全星区 = 4


class 信息等级(IntEnum):
    不常显信息 = 0
    常显图标 = 1
    常显标题 = 2
    常显待办事项 = 3
