from typing import Union

import mod兼容
import 日志
from 蓝图格式.序号字典.模型与序号 import 序号转模型, 模型转序号
from 蓝图格式.序号字典.绰号转真名 import 绰号转真名
from 蓝图格式.蓝图基础类型 import 蓝图基类

# from 蓝图格式.模型 import 模型
class 模型(蓝图基类):
    # 基础功能 #
    def __init__(self, 标识: Union[int, str]):
        if isinstance(标识, str):
            if 标识.isdigit():
                self.序号 = int(标识) 
            else:
                self.序号 = 模型.名字转序号(标识)
        elif isinstance(标识, int):
            self.序号 = 标识
        else:
            raise TypeError("输入类型必须是int或str")

    def __hash__(self):
        return hash(self.序号)

    def __repr__(self):
        return 模型.序号转名字(self.序号)

    def __eq__(self, other):
        if isinstance(other, 模型):  # 检查是否是同类实例
            return self.序号 == other.序号
        elif isinstance(other, int):
            return self.序号 == other
        elif isinstance(other, str):
            return 模型.名字转序号(self.序号) == other
        else:
            raise TypeError("输入类型必须是int, str 或模型")

    def __asdict__(self):
        return 模型.序号转名字(self.序号)

    @staticmethod
    def 创世序号转名字(序号: int) -> str:
        # 暂时不兼容多版本, 所以隔离
        from 蓝图格式.序号字典.创世之书31_模型与序号 import 创世_序号转模型
        if 序号 in 创世_序号转模型:
            return f"创世之书:{创世_序号转模型[序号]}"
        return None

    @staticmethod
    def 创世名字转序号(名字: str) -> int:
        # 暂时不兼容多版本, 所以隔离
        from 蓝图格式.序号字典.创世之书31_模型与序号 import 创世_模型转序号
        if 名字 in 创世_模型转序号:
            return 创世_模型转序号[名字]
        return None

    @staticmethod
    def 序号转名字(序号: int) -> str:
        if not isinstance(序号, int):
            raise ValueError(f"输入不为整数: {序号}")
        if 序号 in 序号转模型:
            return 序号转模型[序号]
        if mod兼容.当前mod类型() == mod兼容.mod类型.创世之书31:
            名字 = 模型.创世序号转名字(序号)
            if 名字 is not None:
                return 名字
        日志.警告(f"未知模型序号: {序号}")
        return f"未知模型:{序号}"

    @staticmethod
    def 作用域加名字转序号(作用域: str, 名字: str) -> int:
        作用域 = 作用域.strip()
        名字 = 名字.strip()
        if 作用域 == "未知模型":
            return int(名字)
        elif 作用域 == "创世之书":
            return 模型.创世名字转序号(名字)
        else:
            raise ValueError(f"未知的模型作用域: {作用域}")

    @staticmethod
    def 名字转序号(名字: str) -> int:
        名字 = 名字.strip()
        if 名字 == "未定义":
            return 0
        elif 名字.isdigit():
            return int(名字) 
        elif ":" in 名字:
            作用域, 名称 = 名字.split(":", 1)
            return 模型.作用域加名字转序号(作用域, 名称)
        elif "：" in 名字:
            作用域, 名称 = 名字.split("：", 1)
            return 模型.作用域加名字转序号(作用域, 名称)
        if 名字 in 绰号转真名:
            名字 = 绰号转真名[名字]
        if 名字 in 模型转序号:
            return 模型转序号[名字]
        if mod兼容.当前mod类型() == mod兼容.mod类型.创世之书31:
            序号 = 模型.创世名字转序号(名字)
            if 序号 is not None:
                return 序号
        raise ValueError(f"未知的模型名字: {名字}")

    def 转蓝图字符串(self) -> str:
        return str(self.序号)

    def 转int(self) -> int:
        return self.序号

    def 转名字(self) -> str:
        return 模型.序号转名字(self.序号)

    def 转json(self) -> str:
        return 模型.序号转名字(self.序号)

    @classmethod
    def 由json转换(cls, 数据字典):
        return 模型(数据字典)

    # 基础功能 #

    # 拓展功能 #
    # 大部分情况下, 模型决定功能而非物品ID。
    # 因此，判定建筑最好用模型序号
    # 硬编码, 有点降低可维护性, 并且没用更清晰易懂的中文, 是基于性能考虑
    # 反正除了创世之书, 没人闲着蛋疼天天动模型ID
    def 是分拣器吗(self):
        # 蓝 绿 黄 白
        return self.序号 in [43, 42, 41, 483]

    def 是传送带吗(self):
        # 蓝 绿 黄
        return self.序号 in [35, 36, 37]

    def 是熔炉吗(self):
        # 红 白
        return self.序号 in [457, 194, 62]

    def 是制造台吗(self):
        # 黑 蓝 绿 黄
        return self.序号 in [456, 67, 66, 65]

    def 是化工厂吗(self):
        # 蓝 白
        return self.序号 in [376, 64]

    def 是研究站吗(self):
        # 黑 白
        return self.序号 in [455, 70]

    def 是制造建筑吗(self):
        # 研究站和分馏塔不算
        return \
            self.是熔炉吗() or \
            self.是制造台吗() or \
            self.是化工厂吗() or \
            self.序号 in [63, 69] # 是原油萃取站吗或量子对撞机吗

    def 是塔吗(self):
        # 小塔 大塔
        # 严格意义上 轨道采集器和大型采矿机也算塔。
        # 但这里先不算了
        return self.序号 in [49, 50]

    def 是箱子吗(self):
        return self.序号 in [51, 52]

    def 是四向吗(self):
        return self.序号 in [38, 39, 40]
    
    def 是炮塔吗(self):
        """判断是否是防御炮塔（高斯机枪塔/高频激光塔/聚爆加农炮/导弹防御塔/近程电浆塔/磁化电浆炮）"""
        return self.序号 in [373, 374, 375, 407, 408, 482]
