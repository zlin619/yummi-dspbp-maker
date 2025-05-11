from 日志 import 确保类型, 纯虚函数, 警告
from 蓝图格式.建筑 import 建筑, 建筑主导接口
from 蓝图格式.接口分析.单接口分析 import 接口主导者, 接口方向

# 目前本文件官杀不管埋
# 用完后请重新分析
class 任意建筑:
    def __init__(self, l_建筑: 建筑):
        确保类型(l_建筑, 建筑)
        self.当前建筑 = l_建筑

    def _修改主动接口信息到指定接口(self, 主动接口信息: 建筑主导接口, 输入建筑序号: int, 新目标接口: int, 新自身接口: int):
        主动接口信息.目标序号 = 输入建筑序号
        主动接口信息.目标接口 = 新目标接口
        主动接口信息.目标接口 = 新自身接口

    def 主动输出到指定接口(self, 输入建筑序号: int, 新目标接口: int, 新自身接口: int):
        self._修改主动接口信息到指定接口(self.当前建筑.输出接口, 输入建筑序号, 新目标接口, 新自身接口)
                
    def 主动输入到指定接口(self, 输入建筑序号: int, 新目标接口: int, 新自身接口: int):
        self._修改主动接口信息到指定接口(self.当前建筑.输入接口, 输入建筑序号, 新目标接口, 新自身接口)

    def 修改主动输出到任意接口(self, 输入建筑: 建筑):
        pass
    def 修改主动输入到任意接口(self, 输出建筑: 建筑):
        pass
    def 修改主动输出到传送带(self, 输入建筑: 建筑):
        pass
    def 修改主动输入到传送带(self, 输出建筑: 建筑):
        pass
    def 断开输入(self):
        pass
    def 断开输出(self):
        pass
    def 断开全部连接(self):
        pass

class 分拣器(任意建筑):
    def 修改输出到传送带(输入建筑):
        pass
    def 修改输入到传送带(输出建筑):
        pass
    def 主动输出到(self, 输入建筑序号: int, 新目标接口: int, 新自身接口: int):
        pass
    def 修改输入到(输出建筑):
        pass
    def 输出到(输入建筑):
        pass
    def 输入到(输出建筑):
        pass
    def 断开输入():
        pass
    def 断开输出():
        pass

class 传送带(任意建筑):
    def 修改输出到(输入建筑):
        pass
    def 修改输入到(输出建筑):
        pass
    def 断开输入():
        pass
    def 断开输出():
        pass

class 一般建筑(任意建筑):
    def 修改输出到任意接口(输入建筑):
        pass
    def 修改输入到任意接口(输出建筑):
        pass
    def 修改输出到传送带(输入建筑):
        pass
    def 修改输入到传送带(输出建筑):
        pass
    def 修改输出为(输入建筑):
        pass
    def 修改输入为(输出建筑):
        pass
    def 修改堆叠为(堆叠目标):
        pass
    def 断开输入():
        pass
    def 断开输出():
        pass

class 单出口建筑(任意建筑):
    def 修改输出到任意接口(输入建筑):
        pass
    def 修改输入到任意接口(输出建筑):
        pass
    def 修改输出到传送带(输入建筑):
        pass
    def 修改输入到传送带(输出建筑):
        pass
    def 修改输出为(输入建筑):
        pass
    def 修改输入为(输出建筑):
        pass
    def 修改堆叠为(堆叠目标):
        pass
    def 断开输入():
        pass
    def 断开输出():
        pass