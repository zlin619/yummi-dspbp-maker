import 日志
from 蓝图格式.蓝图 import 图标
from 蓝图格式.建筑 import 建筑
from 蓝图格式.坐标 import 普通建筑姿态
from 蓝图格式.坐标 import 传送带姿态
from 蓝图格式.坐标 import 分拣器姿态
from 蓝图格式.坐标 import 全空间姿态
from 功能.格式查找 import 蓝图内查找

from typing import Any, List


# 简单替换物品ID会原地爆炸
# 因为建筑的姿态(坐标和旋转)跟着itmID走
# 而且这个字段不一样长
class 物品替换():
    def __init__(self, 输入数据: 建筑):
        if not isinstance(输入数据, 建筑):
            raise TypeError("只有建筑方可替换")
        self._建筑 = 输入数据
        self._姿态数组 = self._建筑.空间姿态.转数组()

    def 强行转换(self, 物品ID: 图标):
        self._建筑.物品序号 = 物品ID

    def 为普通建筑(self, 物品ID: 图标):
        if self._建筑.物品序号.是传送带吗() or self._建筑.物品序号.是分拣器吗():
            self._建筑.空间姿态 = 普通建筑姿态(
                东西X=self._姿态数组[0],
                南北Y=self._姿态数组[1],
                高度Z=self._姿态数组[2],
                水平旋转Z=self._姿态数组[3]
            )
        self._建筑.物品序号 = 物品ID

    def 为传送带(self, 物品ID: 图标):
        if not self._建筑.物品序号.是传送带吗():
            self._姿态数组.append(0)
            self._建筑.空间姿态 = 传送带姿态(
                东西X=self._姿态数组[0],
                南北Y=self._姿态数组[1],
                高度Z=self._姿态数组[2],
                水平旋转Z=self._姿态数组[3],
                左右倾斜X=self._姿态数组[4]
            )
        self._建筑.物品序号 = 物品ID
        return self._建筑

    def 为分拣器(self, 物品ID: 图标):
        if not self._建筑.物品序号.是分拣器吗():
            self._姿态数组.append(0)
            self._姿态数组.append(0)
            self._姿态数组 = self._姿态数组[:6]
            l_起点 = 全空间姿态(*self._姿态数组)
            l_终点 = l_起点.copy()
            self._建筑.姿态 = 分拣器姿态(起点 = l_起点, 终点 = l_终点)
        self._建筑.物品序号 = 物品ID

    def 为(self, 物品ID: 图标):
        前物品ID = self._建筑.物品序号
        if 前物品ID == 物品ID:
            return
        if self._建筑.模型序号.是分拣器吗() and not 物品ID.是分拣器吗():
            日志.警告("分拣器的物品替换为非分拣器时, 可能会出现长度或者其他问题")
        if 物品ID.是传送带吗():
            return self.为传送带(物品ID)
        elif 物品ID.是分拣器吗():
            return self.为分拣器(物品ID)
        else:
            return self.为普通建筑(物品ID)

