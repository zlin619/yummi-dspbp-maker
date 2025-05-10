from 蓝图格式.区域 import 区域
from 蓝图格式.蓝图 import 蓝图
from 蓝图格式.坐标 import 传送带姿态
from 蓝图格式.坐标 import 普通建筑姿态
from 功能.格式查找 import 蓝图内查找

def 舍弃精度(输入, 精度容忍=1/1024):
    近似 = round(输入)
    if abs(输入 - 近似) < 精度容忍:
        return 近似
    八倍 = 输入 * 8
    八倍近似 = round(八倍)
    if abs(八倍 - 八倍近似) < 精度容忍 / 8:
        return 八倍近似 / 8
    return 输入

class 批量舍弃精度:
    def __init__(self, 输入数据):
        self.所有建筑 = 蓝图内查找(输入数据).所有建筑()

    def 坐标(self, 精度容忍=1/256):
        for 单个建筑 in self.所有建筑:
            当前姿态 = 单个建筑.空间姿态
            if isinstance(当前姿态, 普通建筑姿态) or isinstance(当前姿态, 传送带姿态):
                当前姿态 = 单个建筑.空间姿态
                当前姿态.东西X = 舍弃精度(当前姿态.东西X, 精度容忍)
                当前姿态.南北Y = 舍弃精度(当前姿态.南北Y, 精度容忍)
                当前姿态.高度Z = 舍弃精度(当前姿态.高度Z, 精度容忍)
        return self

    def 旋转(self, 精度容忍=1/64):
        for 单个建筑 in self.所有建筑:
            当前姿态 = 单个建筑.空间姿态
            if isinstance(当前姿态, 普通建筑姿态):
                当前姿态.水平旋转Z = 舍弃精度(当前姿态.水平旋转Z, 精度容忍)
            elif isinstance(当前姿态, 传送带姿态):
                当前姿态.水平旋转Z = 舍弃精度(当前姿态.水平旋转Z, 精度容忍)
                当前姿态.左右倾斜X = 舍弃精度(当前姿态.左右倾斜X, 精度容忍)
            else:
                # 懒得写
                pass
        return self

