# from typing import Optional
# from typing import Type
from dataclasses import dataclass
from enum import IntEnum

from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类

class 分组模式(IntEnum):
    不分组 = 0
    分组1 = 1
    分组2 = 2
    分组3 = 3
    分组4 = 4
    分组5 = 5

class 攻击优先级(IntEnum):
    关闭 = 0
    低优先 = 1
    均衡 = 2
    高优先 = 3

@dataclass
class 攻击设置(蓝图dataclass基类):
    地面优先级: 攻击优先级
    低空优先级: 攻击优先级
    高空优先级: 攻击优先级
    太空优先级: 攻击优先级

    @staticmethod
    def 由int构造(入参int32):
        return 攻击设置(
            地面优先级 = 攻击优先级((入参int32 >> 0) & 0b11),
            低空优先级 = 攻击优先级((入参int32 >> 2) & 0b11),
            高空优先级 = 攻击优先级((入参int32 >> 4) & 0b11),
            太空优先级 = 攻击优先级((入参int32 >> 6) & 0b11),
        )

    def 转int(self) -> int:
        return (
            (int(self.地面优先级) << 0) |
            (int(self.低空优先级) << 2) |
            (int(self.高空优先级) << 4) |
            (int(self.太空优先级) << 6)
        )
