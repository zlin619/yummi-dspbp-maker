from dataclasses import dataclass
from enum import IntEnum, auto
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类
from 蓝图格式 import 类型
from 蓝图格式.模型 import 模型

import 日志

class 接口类型(IntEnum):
    未知 = auto()
    堆叠 = auto()
    传送带 = auto()
    分拣器 = auto()
    传送带之间 = auto()
    传送带对普通建筑 = auto()

class 接口主导者(IntEnum):
    自身 = 0
    目标 = 1
    未知 = -1

class 接口方向(IntEnum):
    自身流向目标 = 0
    目标流向自身 = 1
    未知 = -1

@dataclass
class 建筑预览(蓝图dataclass基类):
    建筑序号: 类型.Int32
    模型序号: 模型

    @staticmethod
    def 由建筑构造(输入建筑):
        return 建筑预览(
            建筑序号 = 输入建筑.建筑序号,
            模型序号 = 输入建筑.模型序号
        )

    @staticmethod
    def 空预览():
        return 建筑预览(
            建筑序号 = 类型.Int32(-1),
            模型序号 = 模型("未定义")
        )

    def 为空(self):
         # 建筑序号 -1 表示无建筑/未分析
        return self.建筑序号 == -1
    
    def 转json(self):
        if self.为空():
            return None
        else:
            return self.原始函数_转json()

@dataclass
class 单接口分析(蓝图dataclass基类):
    自身接口序号: 类型.Int8
    目标接口序号: 类型.Int8
    主导者: 接口主导者
    连接方向: 接口方向
    自身建筑: 建筑预览
    连接建筑: 建筑预览
    起点建筑: 建筑预览
    终点建筑: 建筑预览
    连接类型: 接口类型

    @classmethod
    def 由json转换(cls, 数据字典):
        # 不如重测
        return None

