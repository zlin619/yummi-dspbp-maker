from typing import Union

import 日志
from 蓝图格式.序号字典.图标与序号 import 序号转图标
from 蓝图格式.序号字典.图标与序号 import 建筑转序号, 纯物品转序号, 纯图标转序号, 高效配方转序号, 科技转序号, 图标转序号
from 蓝图格式.序号字典.绰号转真名 import 绰号转真名
from 蓝图格式.蓝图基础类型 import 蓝图基类

# from 蓝图格式.图标 import 图标
class 图标(蓝图基类):
    # 图标包含四大类
    # 1.纯图标 0-999
    # 2.物品图标 1000-9999
    # 3.高效配方图标
    # 4.科技图标
    def __init__(self, 标识: Union[int, str]):
        if isinstance(标识, str):
            if 标识.isdigit():
                self.序号 = int(标识) 
            else:
                self.序号 = 图标.名字转序号(标识)
        elif isinstance(标识, int):
            self.序号 = 标识
        else:
            raise TypeError("输入类型必须是int或str")

    def __hash__(self):
        return hash(self.序号)

    def __repr__(self):
        return 图标.序号转名字(self.序号)

    def __eq__(self, other):
        if isinstance(other, 图标):
            return self.序号 == other.序号
        elif isinstance(other, int):
            return self.序号 == other
        elif isinstance(other, str):
            return 图标.名字转序号(self.序号) == other
        else:
            raise TypeError("输入类型必须是int, str 或图标")

    def __asdict__(self):
        return 图标.序号转名字(self.序号)

    @staticmethod
    def 序号转名字(序号: int) -> str:
        if 序号 in 序号转图标:
            return 序号转图标[序号]
        日志.警告(f"未知图标序号:{序号}")
        return f"未知图标:{序号}"

    @staticmethod
    def 作用域加名字转序号(作用域: str, 名字: str) -> int:
        作用域 = 作用域.strip()
        名字 = 名字.strip()
        if 作用域 == "建筑":
            return 建筑转序号[名字]
        elif 作用域 == "纯物品":
            return 纯物品转序号[名字]
        elif 作用域 == "纯图标":
            return 纯图标转序号[名字]
        elif 作用域 == "高效配方":
            return 高效配方转序号[名字]
        elif 作用域 == "科技":
            return 科技转序号[名字]
        elif 作用域 == "未知图标":
            return int(名字)
        else:
            raise ValueError(f"未知的图标作用域: {作用域}")

    @staticmethod
    def 名字转序号(名字: str) -> int:
        if 名字 == "未定义":
            return 0
        elif ":" in 名字:
            作用域, 名称 = 名字.split(":", 1)
            return 图标.作用域加名字转序号(作用域, 名称)
        elif "：" in 名字:
            作用域, 名称 = 名字.split("：", 1)
            return 图标.作用域加名字转序号(作用域, 名称)

        if 名字 in 绰号转真名:
            名字 = 绰号转真名[名字]

        if 名字 in 图标转序号:
            return 图标转序号[名字]
        raise ValueError(f"未知的图标名字: {名字}")

    @staticmethod
    def 序号转真名(序号: int) -> str:
        名字 = 图标.序号转名字(序号)
        if 名字 == "未定义":
            return "未定义"
        else:
            return 名字.split(":")[1].strip()

    def 转蓝图字符串(self) -> str:
        return str(self.序号)

    def 转int(self) -> int:
        return self.序号

    def 转名字(self) -> str:
        return 图标.序号转名字(self.序号)

    def 转真名(self) -> str:
        return 图标.序号转真名(self.序号)

    def 转json(self) -> str:
        return 图标.序号转名字(self.序号)

    @classmethod
    def 由json转换(cls, 数据字典):
        return 图标(数据字典)

    # 基础功能 #

    # 拓展功能 #

    # 大部分情况下, 模型决定功能而非物品ID。
    # 因此，判定建筑最好用模型序号
    # 但是姿态是由itemID决定的
    def 是传送带吗(self):
        return 2000 < self.序号 < 2010
    
    def 是分拣器吗(self):
        return 2010 <= self.序号 < 2020
    
    def 是四向吗(self):
        return self.序号 == 2020

物品 = 图标
科技 = 图标
