# from typing import Optional
# from typing import Type
import struct
from dataclasses import dataclass
from enum import IntEnum
from itertools import chain
from typing import List

import 蓝图格式.类型 as 类型
from 蓝图格式.图标 import 图标
from 蓝图格式.模型 import 模型
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类
from 蓝图格式.蓝图基础类型 import 布尔值
from 蓝图格式.蓝图基础类型 import 由json转换为类型
from 蓝图格式.物流塔额外参数Util import 物流塔格子
from 蓝图格式.物流塔额外参数Util import 带子出口

@dataclass
class 额外参数(蓝图dataclass基类):
    def 去解析(self):
        raise NotImplementedError(f"谢谢你，这个算虚基类方法，请重写方法。") 

    @classmethod
    def 由json转换(cls, 数据字典):
        if 数据字典["参数类型"] == "未解析":
            return 额外参数之未解析.由json转换(数据字典)
        if 数据字典["参数类型"] == "空白":
            return 额外参数之空白.由json转换(数据字典)
        elif 数据字典["参数类型"] == "传送带":
            return 额外参数之传送带.由json转换(数据字典)
        elif 数据字典["参数类型"] == "分拣器":
            return 额外参数之分拣器.由json转换(数据字典)
        elif 数据字典["参数类型"] == "储液罐":
            return 额外参数之储液罐.由json转换(数据字典)
        elif 数据字典["参数类型"] == "射线接收站":
            return 额外参数之射线接收站.由json转换(数据字典)
        elif 数据字典["参数类型"] == "能量枢纽":
            return 额外参数之能量枢纽.由json转换(数据字典)
        elif 数据字典["参数类型"] == "垂直发射井":
            return 额外参数之垂直发射井.由json转换(数据字典)
        elif 数据字典["参数类型"] == "制造类建筑":
            return 额外参数之制造类建筑.由json转换(数据字典)
        elif 数据字典["参数类型"] == "物流塔":
            return 额外参数之物流塔.由json转换(数据字典)
        else:
            raise NotImplementedError("伪纯虚基类，还想执行方法，想屁吃？")


@dataclass
class 额外参数之未解析(额外参数):
    参数: List[类型.Int32]
    参数长度: int
    参数类型: str = "未解析"

    def 转比特流(self) -> bytes:
        self.长度还原()
        流数据 = bytearray()
        self.参数长度 = len(self.参数)
        流数据.extend(struct.pack("<H", self.参数长度))
        if self.参数长度 > 0:
            流数据.extend(struct.pack(f"{self.参数长度}i", *self.参数))
        return 流数据

    def 长度压缩(self) -> None:
        # 砍掉末尾的0
        最后一个非0数序号 = next(
            (i for i in reversed(range(len(self.参数))) 
            if int(self.参数[i]) != 0
        ), -1)
        self.参数 = self.参数[:最后一个非0数序号 + 1]

    def 长度还原(self) -> None:
        if self.参数长度 < len(self.参数):
            raise ValueError("原始长度不能小于当前长度")
        self.参数.extend([类型.Int32(0)] * (self.参数长度 - len(self.参数)))

    def 转json(self) -> str:
        self.长度压缩()
        return {
            "参数": self.参数,
            "参数长度": self.参数长度,
            "参数类型": self.参数类型,
        }

    @classmethod
    def 由json转换(cls, 数据字典):
        参数 = cls(**数据字典)
        参数.长度压缩()
        return 参数

    def 尝试解析(self, 模型) -> 额外参数:
        self.长度还原()
        if len(self.参数) == 0:
            return 额外参数之空白()
        elif 模型 not in 额外参数对应关系:
            return self
        else:
            return 额外参数对应关系[模型].尝试构造(self)

@dataclass
class 解析后额外参数(额外参数):
    @classmethod
    def 由json转换(cls, 数据字典):
        print(cls)
        print(数据字典)
        return 由json转换为类型(cls, 数据字典)

    def 转比特流(self):
        return self.去解析().转比特流()

@dataclass
class 额外参数之空白(解析后额外参数):
    参数类型: str = "空白"
    def 去解析(self) -> 额外参数之未解析:
        return 额外参数之未解析(参数长度=0, 参数=[])

@dataclass
class 额外参数之传送带(解析后额外参数):
    图标ID: 图标
    图标数字: 类型.Int32
    参数类型: str = "传送带"

    # 注: 如果没图标的传送带没有额外参数的
    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        # 按理说参数长度只应该为0或2,除此以外都是未定义行为
        # 未定义行为, 但是有效
        l_图标ID = 图标(未解析参数.参数[0])
        if len(未解析参数.参数) >= 2:
            l_图标数字 = 类型.Int32(未解析参数.参数[1])
        else:
            l_图标数字 = 类型.Int32(0)
        return cls(图标ID=l_图标ID, 图标数字=l_图标数字)

    def 去解析(self) -> 额外参数之未解析:
        return 额外参数之未解析 (
            参数长度=2,
            参数=[self.图标ID.转int(), self.图标数字]
        )
# 额外参数之传送带 到此为止

@dataclass
class 额外参数之分拣器(解析后额外参数):
    分拣器长度: 类型.Int32  # 分拣器长度 -> 1-3
    参数类型: str = "分拣器"

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        # 按理说参数长度只应该为0或2,除此以外都是未定义行为
        # 未定义行为, 但是有效
        return cls(分拣器长度=类型.Int32(未解析参数.参数[0]))

    def 去解析(self) -> 额外参数之未解析:
        return 额外参数之未解析(参数长度=1, 参数=[self.分拣器长度])

    # 充分利用未定义行为,未经过测试,就先扔这里再说
    def 有损压缩转解析前(self) -> bytes:
        return 额外参数之空白()
# 额外参数之传送带 到此为止

class 储液罐布尔(IntEnum):
    开 = 1
    关 = -1

@dataclass
class 额外参数之储液罐(解析后额外参数):
    输出: 储液罐布尔
    输入: 储液罐布尔
    参数类型: str = "储液罐"

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        # 按理说参数长度只应该为0或2,除此以外都是未定义行为
        # 未定义行为, 但是有效
        return cls(
            输出=储液罐布尔(未解析参数.参数[0]),
            输入=储液罐布尔(未解析参数.参数[1]),
        )

    def 去解析(self) -> 额外参数之未解析:
        return 额外参数之未解析(参数长度=2, 参数=[int(self.输出), int(self.输入)])

class 射线模式(IntEnum):
    直接发电 = 0
    光子生成 = 1208

@dataclass
class 额外参数之射线接收站(解析后额外参数):
    接收模式: 射线模式
    参数类型: str = "射线接收站"

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        return 额外参数之射线接收站(接收模式=射线模式(未解析参数.参数[0]))

    def 去解析(self) -> 额外参数之未解析:
        return 额外参数之未解析(参数长度=1, 参数=[int(self.接收模式)])

class 能量枢纽模式(IntEnum):
    放电 = -1
    待机 = 0
    充电 = 1

@dataclass
class 额外参数之能量枢纽(解析后额外参数):
    模式: 能量枢纽模式
    参数类型: str = "能量枢纽"

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        return cls(模式=能量枢纽模式(未解析参数.参数[0]))

    def 去解析(self) -> 额外参数之未解析:
        return 额外参数之未解析(参数长度=1, 参数=[int(self.模式)])


@dataclass
class 额外参数之垂直发射井(解析后额外参数):
    是否十倍射速: 布尔值  # 沙盒特供
    参数类型: str = "垂直发射井"

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        return cls(是否十倍射速=布尔值(未解析参数.参数[0]))

    def 去解析(self) -> 额外参数之未解析:
        return 额外参数之未解析(参数长度=1, 参数=[int(self.是否十倍射速)])

# 当前不支持
@dataclass
class 额外参数之制造类建筑(解析后额外参数):
    是否生产加速: 布尔值  # 0(否):额外产出 1(是):生产加速
    参数类型: str = "制造类建筑"

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        return cls(是否生产加速=布尔值(未解析参数.参数[0]))

    def 去解析(self) -> 额外参数之未解析:
        return 额外参数之未解析(参数长度=1, 参数=[int(self.是否生产加速)])

@dataclass
class 额外参数之物流塔(解析后额外参数):
    # TODO: 这里物流塔格子和带子出口有32个,在json显示上会非常难看, 作为仙术蓝图制作者会比较不块. 
    # 应当将没使用的格子不放入json
    # 但这不是什么要紧事情, 可以先不做

    格子: List[物流塔格子]  # 	Array(storageNum)	0	192	物品栏位参数
    传送带出口: List[带子出口]  # 	Array(带子出口)	192	320	传送带插槽参数
    每帧耗电_焦耳: int
    本地运输范围: int  # 	本地运输距离的存储方式是100000000*cos(θ)
    星际运输范围_百米: int  # 	星际运输存储方式是百米, 1LY = 2400000M, 无限为 240000000, 也就是100光年
    会从轨道采集器取货: 布尔值
    曲速启用路程M: int  # 	游戏内UI为AU, 1AU = 40000M
    翘曲器必备: 布尔值
    行星运输机起送量百分比: int
    星际运输船起送量百分比: int
    出塔集装层数: int
    采矿速度: int
    行星运输机自动填充: 布尔值
    星际运输船运输机自动填充: 布尔值
    参数类型: str = "物流塔"

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        p = 未解析参数.参数
        return cls(
            格子=[物流塔格子.from_params(p[i * 6 : i * 6 + 5]) for i in range(32)],
            传送带出口=[
                带子出口.from_params(p[192 + i * 4 : 192 + i * 4 + 4]) for i in range(32)
            ],
            每帧耗电_焦耳=p[320],
            本地运输范围=p[321],
            星际运输范围_百米=p[322],
            会从轨道采集器取货=布尔值(p[323]),
            曲速启用路程M=p[324],
            翘曲器必备=布尔值(p[325]),
            行星运输机起送量百分比=p[326],
            星际运输船起送量百分比=p[327],
            出塔集装层数=p[328],
            采矿速度=p[329],
            行星运输机自动填充=布尔值(p[330]),
            星际运输船运输机自动填充=布尔值(p[331]),
        )

    def 转比特流(self) -> bytes:
        print(self)
        params = list(
            chain(
                *[x.to_params() for x in self.格子],
                *[x.to_params() for x in self.传送带出口],
                [
                    self.每帧耗电_焦耳,
                    self.本地运输范围,
                    self.星际运输范围_百米,
                    int(self.会从轨道采集器取货),
                    self.曲速启用路程M,
                    int(self.翘曲器必备),
                    self.行星运输机起送量百分比,
                    self.星际运输船起送量百分比,
                    self.出塔集装层数,
                    self.采矿速度,
                    int(self.行星运输机自动填充),
                    int(self.星际运输船运输机自动填充),
                ],
            )
        )
        params = params + [0] * (2048 - len(params))
        流数据 = bytearray()
        流数据.extend(struct.pack("<H" + "i" * 2048, 2048, *params))
        return 流数据


# 战场分析基站
# 炮台类建筑
# 四向
# 箱子

额外参数对应关系 = {
    模型.名字转序号("传送带"): 额外参数之传送带,
    模型.名字转序号("高速传送带"): 额外参数之传送带,
    模型.名字转序号("极速传送带"): 额外参数之传送带,

    模型.名字转序号("分拣器"): 额外参数之分拣器,
    模型.名字转序号("高速分拣器"): 额外参数之分拣器,
    模型.名字转序号("极速分拣器"): 额外参数之分拣器,
    模型.名字转序号("集装分拣器"): 额外参数之分拣器,

    # 气塔也是塔, 但我不确定是不是这里
    模型.名字转序号("行星内物流运输站"): 额外参数之物流塔,
    模型.名字转序号("星际物流运输站"): 额外参数之物流塔,
    模型.名字转序号("大型采矿机"): 额外参数之物流塔,

    模型.名字转序号("储液罐"): 额外参数之储液罐,
    模型.名字转序号("射线接收站"): 额外参数之射线接收站,
    模型.名字转序号("能量枢纽"): 额外参数之能量枢纽,
    模型.名字转序号("垂直发射井"): 额外参数之垂直发射井,
}
