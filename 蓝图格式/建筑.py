import struct
from dataclasses import dataclass
from copy import deepcopy
from typing import Any

import 日志
import 蓝图格式.坐标 as 坐标格式
import 蓝图格式.类型 as 类型
from 蓝图格式.图标 import 图标
from 蓝图格式.模型 import 模型
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类
from 蓝图格式.额外参数 import 额外参数

@dataclass
class 建筑主导接口(蓝图dataclass基类):
    目标序号: 类型.Int32 = -1
    目标接口: 类型.Int8 = -1
    自身接口: 类型.Int8 = -1
    插槽偏移: 类型.Int8 = 0
    # 晨隐说插槽偏移常见于分拣器, 但我不知道这玩意干嘛的
    def 为空(self):
        return self.目标序号 == -1

    def 转json(self):
        if self.目标序号 != -1:
            return self.原始函数_转json()
        return {
            "目标序号": "未连接",
            "目标接口": self.目标接口,
            "自身接口": self.自身接口,
            "插槽偏移": self.插槽偏移
        }

    @classmethod
    def 由json转换(cls, 数据字典: dict):
        if 数据字典["目标序号"] == "未连接":
            数据字典["目标序号"] = -1
        return cls.原始函数_由json转换(数据字典)

@dataclass
class 建筑(蓝图dataclass基类):
    建筑序号: 类型.Int32
    区域序号: 类型.Int8

    物品序号: 图标
    模型序号: 模型

    # 原版蓝图根据物品序号解析
    # 蓝图工具根据解析方式解析
    空间姿态: 坐标格式.姿态

    输出接口: 建筑主导接口
    输入接口: 建筑主导接口

    配方序号: 类型.UInt16  # 常见于制造厂类建筑
    过滤物品序号: 图标  # UInt16,常见于分拣器、四向
    额外参数: 额外参数

    # TODO:
    # 以下并非正式数据的一部分
    悠米_接口分析: Any = None
    悠米_建筑标记: Any = None
    悠米_玩家标注: Any = None

    ########################
    # 以上为字段，以下为函数 #
    ########################

    @property
    def 堆叠接口(self):
        return self.输入接口

    def 检查姿态(self):
        def 姿态告警():
            日志.告警(f"物品类型{self.物品序号}和空间姿态{self.空间姿态.__class__}不匹配。这可能导致蓝图无法读取。")
            日志.告警(f"建议:from 功能.指鹿为马.通用 import 强制纠正姿态; 强制纠正姿态(蓝图)")
        if self.物品序号.是传送带吗():
            if not isinstance(self.空间姿态, 坐标格式.传送带姿态):
                姿态告警()
        elif self.物品序号.是分拣器吗():
            if not isinstance(self.空间姿态, 坐标格式.分拣器姿态):
                姿态告警()
        else:
            if not isinstance(self.空间姿态, 坐标格式.普通建筑姿态):
                姿态告警()

    def 转比特流(self) -> bytes:
        self.检查姿态()
        流数据 = bytearray()
        流数据.extend(struct.pack("<i", -101))
        流数据.extend(
            struct.pack(
                "<iHHb",
                self.建筑序号,
                self.物品序号.转int(),
                self.模型序号.转int(),
                self.区域序号,
            )
        )
        流数据.extend(self.空间姿态.转比特流())
        流数据.extend(
            struct.pack(
                "<iibbbbbbHH",                
                self.输出接口.目标序号,
                self.输入接口.目标序号,
                self.输出接口.目标接口,
                self.输入接口.目标接口,
                self.输出接口.自身接口,
                self.输入接口.自身接口,
                self.输出接口.插槽偏移,
                self.输入接口.插槽偏移,
                self.配方序号,
                self.过滤物品序号.转int(),
            )
        )
        流数据.extend(self.额外参数.转比特流())
        return 流数据
    # 转比特流 到此为止


    def 转json(self):
        返回值 = self.原始函数_转json()
        if self.物品序号.是传送带吗() or self.物品序号.是分拣器吗():
            return 返回值
        # 创建新字典，按原始顺序重建键
        新返回值 = {}
        for 键值 in 返回值.keys():
            if 键值 == '输出接口':
                新返回值['堆叠接口'] = 返回值[键值]
            else:
                新返回值[键值] = 返回值[键值]
        return 新返回值

    @classmethod
    def 由json转换(cls, 数据字典: dict):
        if '堆叠接口' not in 数据字典:
            return cls.原始函数_由json转换(数据字典)
        新数据字典 = {}
        for 键值 in 数据字典.keys():
            if 键值 == '堆叠接口':
                新数据字典['输出接口'] = 数据字典[键值]
            else:
                新数据字典[键值] = 数据字典[键值]
        return cls.原始函数_由json转换(新数据字典)


# 建筑 到此为止
