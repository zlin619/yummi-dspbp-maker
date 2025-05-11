from dataclasses import dataclass
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类
from 蓝图格式.接口分析.单接口分析 import 单接口分析
# TODO:
import 日志

@dataclass
class 多接口分析(蓝图dataclass基类):
    接口数据: list[单接口分析]

    def __init__(self):
        self.接口数据 = []

    def 添加分析(self, 输入接口: 单接口分析):
        self.接口数据.append(输入接口)

    def 按建筑查找(self, l_建筑序号: int) -> 单接口分析:
        for 接口 in self.接口数据:
            if 接口.连接建筑.建筑序号 == l_建筑序号:
                return 接口
        return None

    def 按自身接口查找(self, l_自身接口序号: int) -> 单接口分析:
        for 接口 in self.接口数据:
            if 接口.自身接口序号 == l_自身接口序号:
                return 接口
        return None

    def 合法校验():
        日志.未完成的函数()

    def 排序():
        日志.未完成的函数()

    def 分拣器数量() -> int:
        日志.未完成的函数()
    
    def 接口序号转建筑(): # 建筑
        from 蓝图格式.建筑 import 建筑
        日志.未完成的函数()

    @classmethod
    def 由json转换(cls, 数据字典):
        # 不如重测
        return None
