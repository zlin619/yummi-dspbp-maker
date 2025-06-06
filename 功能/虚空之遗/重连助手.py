

from 功能.格式查找 import 蓝图内查找
from 蓝图格式 import 类型
from 蓝图格式.建筑 import 建筑, 建筑主导接口
from 蓝图格式.接口分析.多接口分析 import 多接口分析
from 蓝图格式.接口分析.单接口分析 import 单接口分析, 建筑预览, 接口主导者, 接口方向


class 对蓝图中:
    def __init__(self, 蓝图或建筑群):
        self.所有建筑: list[建筑] = 蓝图内查找(蓝图或建筑群).所有建筑()

    def 的某建筑(self, l_自身建筑: 建筑):
        self.主导建筑: 建筑 = l_自身建筑
        self.主导建筑序号 = l_自身建筑.建筑序号
        return self
    
    def 的输入(self):
        self.是输出 = False
        self.被连建筑序号 = self.主导建筑.输入接口.目标序号
        if self.被连建筑序号 != -1:
            self.被连建筑: 建筑 = self.所有建筑[self.被连建筑序号]
            self.查找输出分析()
        return self

    def 的输出(self):
        self.是输出 = True
        self.被连建筑序号: 类型.Int32 = self.主导建筑.输出接口.目标序号
        if self.被连建筑序号 != -1:
            self.被连建筑 = self.所有建筑[self.被连建筑序号]
            self.查找输出分析()
        return self

    def 查找输入分析(self):
        self.自身接口分析 = [
            l_接口 for l_接口 in self.主导建筑.悠米_接口分析.接口数据
            if (
                l_接口.主导者 == 接口主导者.自身
                and l_接口.连接方向 == 接口方向.目标流向自身
                and l_接口.自身建筑.建筑序号 == self.主导建筑序号
                and l_接口.连接建筑.建筑序号 == self.被连建筑序号
            )
        ][0]
        self.对侧接口分析 = [
            l_接口 for l_接口 in self.被连建筑.悠米_接口分析.接口数据
            if (
                l_接口.主导者 == 接口主导者.目标
                and l_接口.连接方向 == 接口方向.自身流向目标
                and l_接口.自身建筑.建筑序号 == self.被连建筑序号
                and l_接口.连接建筑.建筑序号 == self.主导建筑序号
            )
        ][0]

    def 查找输出分析(self):
        self.自身接口分析 = [
            l_接口 for l_接口 in self.主导建筑.悠米_接口分析.接口数据
            if (
                l_接口.主导者 == 接口主导者.自身
                and l_接口.连接方向 == 接口方向.自身流向目标
                and l_接口.自身建筑.建筑序号 == self.主导建筑序号
                and l_接口.连接建筑.建筑序号 == self.被连建筑序号
            )
        ][0]
        self.对侧接口分析 = [
            l_接口 for l_接口 in self.被连建筑.悠米_接口分析.接口数据
            if (
                l_接口.主导者 == 接口主导者.目标
                and l_接口.连接方向 == 接口方向.目标流向自身
                and l_接口.自身建筑.建筑序号 == self.被连建筑序号
                and l_接口.连接建筑.建筑序号 == self.主导建筑序号
            )
        ][0]

    def 的单接口分析(self, l_接口分析: 单接口分析):
        if l_接口分析.主导者 == 接口主导者.自身:
            self.主导建筑: 建筑 = self.所有建筑[l_接口分析.自身建筑.建筑序号]
            self.连接建筑: 建筑 = self.所有建筑[l_接口分析.连接建筑.建筑序号]
            if l_接口分析.连接方向 == 接口方向.自身流向目标:
                self.是输出 = True
            elif l_接口分析.连接方向 == 接口方向.目标流向自身:
                self.是输出 = False
            else:
                raise Exception("连接方向未知, 疑似数据损坏")
        elif l_接口分析.主导者 == 接口主导者.目标:
            self.主导建筑: 建筑 = self.所有建筑[l_接口分析.连接建筑.建筑序号]
            self.连接建筑: 建筑 = self.所有建筑[l_接口分析.自身建筑.建筑序号]
            if l_接口分析.连接方向 == 接口方向.自身流向目标:
                self.是输出 = False
            elif l_接口分析.连接方向 == 接口方向.目标流向自身:
                self.是输出 = True
            else:
                raise Exception("连接方向未知, 疑似数据损坏")
        else:
            raise Exception("主导者未知, 疑似数据损坏")
        self.主导建筑序号 = self.主导建筑.建筑序号
        self.连接序号 = self.连接建筑.建筑序号
        if self.是输出:
            self.查找输出分析()
        else:
            self.查找输入分析()

    def 置空(self):
        if self.是输出:
            self.主导建筑.输出接口.目标序号 = -1
        else:
            self.主导建筑.输入接口.目标序号 = -1

    # 对蓝图中(蓝图或建筑群).的某建筑(建筑).的输出().删除()
    def 删除(self) -> None:
        if self.被连建筑序号 == -1:
            return
        self.主导建筑.悠米_接口分析.接口数据.remove(self.自身接口分析)
        self.被连建筑.悠米_接口分析.接口数据.remove(self.对侧接口分析)
        self.置空()

    def _修改主动接口信息到指定接口(self, 主动接口信息: 建筑主导接口, 输入建筑序号: int, 新目标接口: int, 新自身接口: int):
        主动接口信息.目标序号 = 输入建筑序号
        主动接口信息.目标接口 = 新目标接口
        主动接口信息.目标接口 = 新自身接口

    def 主动输出到指定接口(self, 输入建筑序号: int, 新目标接口: int, 新自身接口: int):
        self._修改主动接口信息到指定接口(self.主导建筑.输出接口, 输入建筑序号, 新目标接口, 新自身接口)
                
    def 主动输入到指定接口(self, 输入建筑序号: int, 新目标接口: int, 新自身接口: int):
        self._修改主动接口信息到指定接口(self.主导建筑.输入接口, 输入建筑序号, 新目标接口, 新自身接口)
