from 蓝图格式.蓝图 import 图标
from 蓝图格式.建筑 import 建筑
from 功能.格式查找 import 蓝图内查找
from typing import Any, List


def _镜花水月(所有建筑: List[建筑]) -> None:
    for 当前建筑 in 所有建筑:
        当前建筑.物品序号 = 图标("水")

def 镜花水月(输入数据: Any) -> None:
    _镜花水月(蓝图内查找(输入数据).l_所有建筑)
