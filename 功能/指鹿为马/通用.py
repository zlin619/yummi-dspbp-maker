import copy
import 日志
from 蓝图格式.蓝图基础类型 import 布尔值
from 蓝图格式.蓝图 import 图标
from 蓝图格式.建筑 import 建筑, 建筑类型分析
from 蓝图格式.坐标 import 普通建筑姿态
from 蓝图格式.坐标 import 传送带姿态
from 蓝图格式.坐标 import 分拣器姿态
from 蓝图格式.坐标 import 全空间姿态


# 简单替换物品ID会原地爆炸
# 因为建筑的姿态(坐标和旋转)跟着itmID走
# 而且这个字段不一样长
class 物品替换():
    _建筑: 建筑
    _姿态数组: list[float]
    _修改姿态: 布尔值

    def __init__(self, 输入数据: 建筑):
        if not isinstance(输入数据, 建筑):
            raise TypeError("只有建筑方可替换")
        self._建筑 = 输入数据
        self._姿态数组 = self._建筑.空间姿态.转数组()
        self._修改姿态 = 布尔值.否

    def 强行转换(self, 物品ID: 图标):
        if not isinstance(物品ID, 图标):
            raise TypeError("物品ID必须为class图标")
        self._建筑.物品序号 = 物品ID
        return self._修改姿态

    def 为普通建筑(self, 物品ID: 图标):
        日志.确保类型(物品ID, 图标)
        if self._建筑.物品序号.是传送带吗() or self._建筑.物品序号.是分拣器吗():
            self._修改姿态 = 布尔值.是
            self._建筑.空间姿态 = 普通建筑姿态(
                东西X=self._姿态数组[0],
                南北Y=self._姿态数组[1],
                高度Z=self._姿态数组[2],
                水平旋转Z=self._姿态数组[3]
            )
        self._建筑.物品序号 = 物品ID
        return self._修改姿态

    def 为传送带(self, 物品ID: 图标):
        日志.确保类型(物品ID, 图标)
        if not self._建筑.物品序号.是传送带吗():
            self._修改姿态 = 布尔值.是
            self._姿态数组.append(0)
            self._建筑.空间姿态 = 传送带姿态(
                东西X=self._姿态数组[0],
                南北Y=self._姿态数组[1],
                高度Z=self._姿态数组[2],
                水平旋转Z=self._姿态数组[3],
                左右倾斜X=self._姿态数组[4]
            )
        self._建筑.物品序号 = 物品ID
        return self._修改姿态

    def 为分拣器(self, 物品ID: 图标):
        日志.确保类型(物品ID, 图标)
        if not self._建筑.物品序号.是分拣器吗():
            self._修改姿态 = 布尔值.是
            self._姿态数组.append(0)
            self._姿态数组.append(0)
            self._姿态数组 = self._姿态数组[:6]
            l_起点 = 全空间姿态(*self._姿态数组)
            l_终点 = copy.deepcopy(l_起点)
            self._建筑.空间姿态 = 分拣器姿态(起点 = l_起点, 终点 = l_终点)
        self._建筑.物品序号 = 物品ID
        return self._修改姿态

    # 标记拆除，不是真的拆
    def 拆(self):
        self.为普通建筑(图标("植物燃料"))
        self._建筑.悠米_建筑类型 = 建筑类型分析.待拆除
        self._建筑.输入接口.目标序号 = -1
        self._建筑.输出接口.目标序号 = -1
        return self._修改姿态

    def 为(self, 物品ID: 图标|str):
        if isinstance(物品ID, str):
            物品ID = 图标(物品ID)
        日志.确保类型(物品ID, 图标)
        前物品ID = self._建筑.物品序号
        if 前物品ID == 物品ID:
            # 什么都不做
            return self._修改姿态
        if self._建筑.模型序号.是分拣器吗() and not 物品ID.是分拣器吗():
            日志.警告("分拣器的物品替换为非分拣器时, 可能会出现长度或者其他问题")
        if 物品ID.是传送带吗():
            self.为传送带(物品ID)
        elif 物品ID.是分拣器吗():
            self.为分拣器(物品ID)
        else:
            self.为普通建筑(物品ID)
        return self._修改姿态

# from 功能.指鹿为马.通用 import 强制纠正姿态
def 强制纠正姿态(输入参数):
    from 功能.格式查找 import 蓝图内查找
    l_所有建筑 = 蓝图内查找(输入参数).所有建筑()
    for 当前建筑 in l_所有建筑:
        l_修改姿态 = 物品替换(当前建筑).为(当前建筑.物品序号)
        if l_修改姿态 == 布尔值.是:
            日志.调试(f"强制纠正了建筑姿态 :序号{当前建筑.建筑序号}, 物品类型{当前建筑.物品序号}, 模型类型{当前建筑.模型序号}")
