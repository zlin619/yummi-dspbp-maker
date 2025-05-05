
from 蓝图格式.中段 import 蓝图中段
from 蓝图格式.蓝图 import 蓝图
from 蓝图格式.建筑 import 建筑
from 蓝图格式.区域 import 区域

# 用法  查找(蓝图).所有区域()
class 蓝图内查找:
    def __init__(self, 输入数据):
        if isinstance(输入数据, 蓝图):
            self.l_本蓝图 = 输入数据
        elif isinstance(输入数据, 蓝图中段):
            self.l_本蓝图中段 = 输入数据
        elif isinstance(输入数据, list):
            if len(输入数据) == 0:
                raise Exception("你输入了一个空list, 但是list所有建筑和list所有区域都不可能为空")
            elif isinstance(输入数据[0], 区域):
                self.l_所有区域 = 输入数据
            elif isinstance(输入数据[0], 建筑):
                self.l_所有建筑 = 输入数据
            else:
                raise Exception("鬼知道你输入了个什么东西")

    def 本蓝图(self):
        if not hasattr(self, '蓝图'):
            raise Exception("啥都没有找个锤子")
        return self.l_所有区域

    def 本蓝图中段(self):
        if not hasattr(self, '所有区域'):
            self.l_本蓝图中段 = self.本蓝图().蓝图中段
            return self.l_本蓝图中段

    def 所有区域(self):
        if not hasattr(self, '所有区域'):
            self.l_所有区域 = self.本蓝图中段().区域
            return self.l_所有区域
        
    def 所有建筑(self):
        if not hasattr(self, '所有区域'):
            self.l_所有区域 = self.本蓝图中段().建筑
            return self.l_所有区域