# 镜花水月: 指所有建筑都造不出来
from 蓝图格式.蓝图 import 蓝图
from 蓝图格式.蓝图 import url字符串
from 蓝图格式.图标 import 图标
from 功能.mod兼容 import mod类型
from 功能.mod兼容 import 当前mod类型
from 功能.格式查找 import 蓝图内查找
from 功能.指鹿为马.通用 import 物品替换

# 记得四向分流器
def 接口测序(输入数据: 蓝图) -> None:
    所有建筑 = 蓝图内查找(输入数据).所有建筑()
    for 当前建筑 in 所有建筑:
        l_物品序号名称 = 当前建筑.物品序号.转名字()
        if 当前建筑.物品序号.是四向吗() and 当前建筑.模型序号.是四向吗():
            pass
        elif l_物品序号名称 != 当前建筑.模型序号.转名字():
            continue


