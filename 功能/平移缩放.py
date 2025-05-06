# 建议先运行单格锚点
from 蓝图格式.坐标 import 空间坐标
from 蓝图格式.坐标 import Int16平面坐标
from 功能.格式查找 import 蓝图内查找

class 平移缩放:
    def __init__(self, l_输入参数):
        self.输入参数 = l_输入参数

    # 坐标=空间坐标(东西X = 3, 南北Y = 1.3, 高度Z = 0)
    def 建筑平移(self, 输入坐标: 空间坐标):
        所有建筑 = 蓝图内查找(self.输入参数).所有建筑()
        for 当前建筑 in 所有建筑:
            当前建筑.空间姿态.坐标平移(输入坐标)
        return self

    def 区域平移(self, 输入坐标: Int16平面坐标):
        所有区域 = 蓝图内查找(self.输入参数).所有区域()
        for 当前区域 in 所有区域:
            当前区域.锚点偏移.坐标平移(输入坐标)
        return self

    def 建筑缩放(self, 输入坐标: 空间坐标):
        所有建筑 = 蓝图内查找(self.输入参数).所有建筑()
        for 当前建筑 in 所有建筑:
            当前建筑.空间姿态.坐标缩放(输入坐标)
        return self

    def 区域缩放(self, 输入坐标: Int16平面坐标):
        所有区域 = 蓝图内查找(self.输入参数).所有区域()
        for 当前区域 in 所有区域:
            当前区域.锚点偏移.坐标缩放(输入坐标)
        return self
