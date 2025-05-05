# from typing import Optional
# from typing import Type
import struct
from dataclasses import dataclass
from enum import Enum
from itertools import chain
from typing import List

import 蓝图格式.类型 as 类型
from 蓝图格式.图标 import 图标
from 蓝图格式.模型 import 模型
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类, 蓝图基类


@dataclass
class 额外参数(蓝图dataclass基类):
    def 转比特流(self) -> bytes:
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
    参数类型: str = "未解析"

    def 转比特流(self) -> bytes:
        流数据 = bytearray()
        参数长度 = len(self.参数)
        流数据.extend(struct.pack("<H", 参数长度))
        if 参数长度 > 0:
            流数据.extend(struct.pack(f"{参数长度}i", *self.参数))
        return 流数据

    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)

    def 尝试解析(self, 模型) -> 额外参数:
        if len(self.参数) == 0:
            return 额外参数之空白()
        elif 模型 not in 额外参数对应关系:
            return self
        else:
            return 额外参数对应关系[模型].尝试构造(self)


@dataclass
class 额外参数之空白(额外参数):
    参数类型: str = "空白"

    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)

    def 转比特流(self) -> bytes:
        流数据 = bytearray()
        流数据.extend(struct.pack("<H", 0))
        return 流数据


@dataclass
class 额外参数之传送带(额外参数):
    图标ID: 图标
    图标数字: 类型.Int32
    参数类型: str = "传送带"

    # 注: 如果没图标的传送带没有额外参数的
    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        # 按理说参数长度只应该为0或2,除此以外都是未定义行为
        # 未定义行为, 但是有效
        l_图标ID = 图标(未解析参数.参数[0])
        if len(未解析参数.参数) >= 2:
            l_图标数字 = 类型.Int32(未解析参数.参数[1])
        else:
            l_图标数字 = 类型.Int32(0)
        return 额外参数之传送带(图标ID=l_图标ID, 图标数字=l_图标数字)

    def 转比特流(self) -> bytes:
        流数据 = bytearray()
        流数据.extend(struct.pack("<Hii", 2, self.图标ID.转int(), self.图标数字))
        return 流数据

    # 充分利用未定义行为,未经过测试,就先扔这里再说
    def 有损压缩转解析前(self) -> bytes:
        if self.图标ID.转int() == 0:
            return 额外参数之空白()
        elif self.图标数字 == 0:
            return 额外参数之未解析([类型.Int32(self.图标ID.转int())])


@dataclass
class 额外参数之分拣器(额外参数):
    分拣器长度: 类型.Int32  # 分拣器长度 -> 1-3
    参数类型: str = "分拣器"

    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        # 按理说参数长度只应该为0或2,除此以外都是未定义行为
        # 未定义行为, 但是有效
        return 额外参数之分拣器(分拣器长度=类型.Int32(未解析参数.参数[0]))

    def 转比特流(self) -> bytes:
        流数据 = bytearray()
        流数据.extend(
            struct.pack(
                "<Hi",
                1,
                self.分拣器长度,
            )
        )
        return 流数据

    # 充分利用未定义行为,未经过测试,就先扔这里再说
    def 有损压缩转解析前(self) -> bytes:
        return 额外参数之空白()


@dataclass
class 额外参数之储液罐(额外参数):
    是否输出: bool
    是否输入: bool
    参数类型: str = "储液罐"

    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)


@dataclass
class 额外参数之射线接收站(额外参数):
    是否光子生成: bool  # 0(否):直接发电 1208(是):光子生成
    参数类型: str = "射线接收站"

    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)


@dataclass
class 额外参数之能量枢纽(额外参数):
    模式: 类型.Int32  # -1:放电 0:待机 1:充电
    参数类型: str = "能量枢纽"

    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)


@dataclass
class 额外参数之垂直发射井(额外参数):
    是否十倍射速: bool
    参数类型: str = "垂直发射井"

    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)


@dataclass
class 额外参数之制造类建筑(额外参数):
    是否生产加速: bool  # 0(否):额外产出 1(是):生产加速
    参数类型: str = "制造类建筑"

    @classmethod
    def 由json转换(cls, 数据字典):
        return cls(**数据字典)


# 电磁轨道弹射器
# 流速监测器
# 物流配送器


# 塔
class BpEnumMixIn(蓝图基类):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def 转json(self):
        return self.name

    @classmethod
    def 由json转换(cls, name):
        return cls[name]

    def __repr__(self):
        return Enum.__repr__(self)

    __eq__ = Enum.__eq__


class Role(BpEnumMixIn, Enum):
    STORAGE = 0
    SUPPLY = 1
    DEMAND = 2


class LockAmount(BpEnumMixIn, Enum):
    NOTSET = 0
    FULL = 1
    HALF = 2
    EMPTY = 3


class Direction(BpEnumMixIn, Enum):
    NOTSET = 0
    IN = 1
    OUT = 2


ItemID = 图标


@dataclass
class Storage(蓝图dataclass基类):
    item_id: ItemID
    local_role: Role
    remote_role: Role
    max: int
    lockAmount: LockAmount

    @classmethod
    def from_params(cls, p):
        return cls(ItemID(p[0]), Role(p[1]), Role(p[2]), p[3], LockAmount(p[4]))

    def to_params(self):
        return [
            self.item_id.序号,
            self.local_role.value,
            self.remote_role.value,
            self.max,
            self.lockAmount.value,
            0,
        ]


@dataclass
class Slot(蓝图dataclass基类):
    dir: Direction
    storage_idx: int

    @classmethod
    def from_params(cls, p):
        return cls(Direction(p[0]), p[1])

    def to_params(self):
        return [
            self.dir.value,
            self.storage_idx,
            0,
            0,
        ]


@dataclass
class 额外参数之物流塔(额外参数):
    storage: List[Storage]  # 	Array(storageNum)	0	192	物品栏位参数
    slots: List[Slot]  # 	Array(slotsNum)	192	320	传送带插槽参数
    work_energy_per_tick: int
    trip_range_of_drones: int
    trip_range_of_ships: int
    include_orbit_collector: bool
    warp_enable_distance: int
    warper_necessary: int
    delivery_amount_of_drones: int
    delivery_amount_of_ships: int
    piler_count: int
    mining_speed: int
    drone_auto_replenish: bool
    ship_auto_replenish: bool
    参数类型: str = "物流塔"

    @classmethod
    def 由json转换(cls, data_dict):
        data_dict["storage"] = [Storage.由json转换(s) for s in data_dict["storage"]]
        data_dict["slots"] = [Slot.由json转换(s) for s in data_dict["slots"]]
        return cls(**data_dict)

    @classmethod
    def 尝试构造(cls, 未解析参数: 额外参数之未解析) -> 额外参数:
        p = 未解析参数.参数
        return cls(
            storage=[Storage.from_params(p[i * 6 : i * 6 + 5]) for i in range(32)],
            slots=[
                Slot.from_params(p[192 + i * 4 : 192 + i * 4 + 4]) for i in range(32)
            ],
            work_energy_per_tick=p[320],
            trip_range_of_drones=p[321],
            trip_range_of_ships=p[322],
            include_orbit_collector=bool(p[323]),
            warp_enable_distance=p[324],
            warper_necessary=p[325],
            delivery_amount_of_drones=p[326],
            delivery_amount_of_ships=p[327],
            piler_count=p[328],
            mining_speed=p[329],
            drone_auto_replenish=bool(p[330]),
            ship_auto_replenish=bool(p[331]),
        )

    def 转比特流(self) -> bytes:
        params = list(
            chain(
                *[x.to_params() for x in self.storage],
                *[x.to_params() for x in self.slots],
                [
                    self.work_energy_per_tick,
                    self.trip_range_of_drones,
                    self.trip_range_of_ships,
                    int(self.include_orbit_collector),
                    self.warp_enable_distance,
                    self.warper_necessary,
                    self.delivery_amount_of_drones,
                    self.delivery_amount_of_ships,
                    self.piler_count,
                    self.mining_speed,
                    int(self.drone_auto_replenish),
                    int(self.ship_auto_replenish),
                ],
            )
        )
        params = params + [0] * (2048 - len(params))
        print(params)
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
    模型.名字转序号("行星内物流运输站"): 额外参数之物流塔,
    模型.名字转序号("星际物流运输站"): 额外参数之物流塔,
    模型.名字转序号("大型采矿机"): 额外参数之物流塔,
}
