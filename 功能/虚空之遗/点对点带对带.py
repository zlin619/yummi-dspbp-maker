from 功能.格式查找 import 蓝图内查找
import 日志
from 蓝图格式.图标 import 图标
from 蓝图格式.序号字典 import 图标与序号
from 蓝图格式.建筑 import 建筑
from 蓝图格式.蓝图 import 蓝图
from 蓝图格式.额外参数 import 额外参数之传送带

# 我不打算让这个文件from import, 而是import
class 一个目标点:
    图标数字: int
    断开连接: set[建筑]
    连接到: 建筑 # | None
    def __init__(self, l_图标数字):
        self.图标数字 = l_图标数字
        self.断开连接 = set()
        self.连接到 = None
    def __hash__(self):
        return hash(self.图标数字)

class 全部连接:
    l_查找数据: set[一个目标点]

    def 查找或新建(self, l_图标数字: 图标) -> 一个目标点:
        for 连接组 in self.l_查找数据:
            if 连接组.图标数字 == l_图标数字:
                return 连接组
        新连接组 = 一个目标点(l_图标数字)
        self.l_查找数据.add(新连接组)
        return 新连接组

    def 查找连接(self, 输入数据: 蓝图) -> None:
        self.l_查找数据 = set()
        所有建筑 = 蓝图内查找(输入数据).所有建筑()
        for 当前建筑 in 所有建筑:
            if not 当前建筑.模型序号.是传送带吗():
                continue
            if not isinstance(当前建筑.额外参数, 额外参数之传送带):
                continue
            l_图标ID : 图标 = 当前建筑.额外参数.图标ID
            l_图标数字 : 图标 = 当前建筑.额外参数.图标数字
            if l_图标ID == 图标与序号('纯图标:目标点'):
                连接组: 一个目标点 = self.查找或新建(self.l_查找数据, l_图标数字)
                if 连接组.断开连接 != None:
                    日志.警告(F"有两个同样数字的连接到: {连接组.连接到.建筑序号} {当前建筑.建筑序号}")
                连接组.连接到 = 当前建筑
            elif l_图标ID == 图标与序号('纯图标:断开连接'):
                连接组: 一个目标点 = self.查找或新建(self.l_查找数据, l_图标数字)
                连接组.断开连接.add(当前建筑)
            else:
                pass
