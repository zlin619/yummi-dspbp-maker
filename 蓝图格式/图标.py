from typing import Union

import 日志
from 蓝图格式.序号字典.图标转序号 import 图标转序号
from 蓝图格式.序号字典.序号转图标 import 序号转图标
from 蓝图格式.序号字典.绰号转真名 import 绰号转真名
from 蓝图格式.蓝图基础类型 import 蓝图基类


class 图标(蓝图基类):
    # 图标包含四大类
    # 1.纯图标 0-999
    # 2.物品图标 1000-9999
    # 3.高效配方图标
    # 4.科技图标
    def __init__(self, 标识: Union[int, str]):
        if isinstance(标识, int):
            self.序号 = 标识
        elif isinstance(标识, str):
            self.序号 = 图标.名字转序号(标识)
        else:
            raise TypeError("输入类型必须是int或str")

    def __repr__(self):
        return 图标.序号转名字(self.序号)

    def __eq__(self, other):
        if isinstance(other, 图标):  # 检查是否是同类实例
            return self.序号 == other.序号
        elif isinstance(other, int):
            return self.序号 == other
        elif isinstance(other, str):
            return 图标.名字转序号(self.序号) == other  # todo:参数应为str但实际有可能为int
        else:
            raise TypeError("输入类型必须是int, str 或图标")

    def __asdict__(self):
        return 图标.序号转名字(self.序号)

    @staticmethod
    def 序号转名字(序号: int) -> str:
        if 序号 in 序号转图标:
            return 序号转图标[序号]
        日志.警告(f"未知图标序号: {序号}")
        return f"未知图标{序号}"

    @staticmethod
    def 名字转序号(名字: str) -> int:
        if 名字.startswith("未知图标"):
            return int(名字[4:])

        if 名字 in 绰号转真名:
            名字 = 绰号转真名[名字]

        if 名字 in 图标转序号:
            return 图标转序号[名字]
        raise ValueError(f"未知的图标名字: {名字}")

    def 转蓝图字符串(self) -> str:
        return str(self.序号)

    def 转int(self) -> int:
        return self.序号

    def 转json(self):
        return 图标.序号转名字(self.序号)

    @classmethod
    def 由json转换(cls, 数据字典):
        return 图标(数据字典)
