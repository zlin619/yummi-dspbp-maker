import struct
from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Any
import 日志
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类
from 蓝图格式.图标 import 图标
from 蓝图格式.模型 import 模型
from 蓝图格式.配方 import 配方
from 蓝图格式.额外参数 import 额外参数
from 蓝图格式.接口分析.多接口分析 import 多接口分析
import 蓝图格式.坐标 as 坐标格式
import 蓝图格式.类型 as 类型

class 建筑类型分析(IntEnum):
    未分析 = auto()
    未知 = auto()
    无特殊性 = auto()
    待拆除 = auto()
    仙术地基 = auto()
    浮空建筑 = auto()
    堆叠建筑 = auto()

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

    配方序号: 配方  # 常见于制造厂类建筑
    过滤物品序号: 图标  # UInt16,常见于分拣器、四向
    额外参数: 额外参数
    额外文本内容: str # V0.10.34.28281新增：建筑额外文本（如信标说明）

    # 以下并非正式数据的一部分
    悠米_接口分析: 多接口分析
    悠米_建筑类型: 建筑类型分析
    悠米_玩家标注: Any = None

    ########################
    # 以上为字段，以下为函数 #
    ########################
    def __hash__(self):
        return hash(self.建筑序号)

    @property
    def 堆叠接口(self) -> 建筑主导接口:
        return self.输入接口

    def 检查姿态(self):
        def 姿态警告():
            日志.警告(f"物品类型{self.物品序号}和空间姿态{self.空间姿态.__class__}不匹配。这可能导致蓝图无法读取。")
            日志.警告(f"建议:from 功能.指鹿为马.通用 import 强制纠正姿态; 强制纠正姿态(蓝图)")
        if self.物品序号.是传送带吗():
            if not isinstance(self.空间姿态, 坐标格式.传送带姿态):
                姿态警告()
        elif self.物品序号.是分拣器吗():
            if not isinstance(self.空间姿态, 坐标格式.分拣器姿态):
                姿态警告()
        else:
            if not isinstance(self.空间姿态, 坐标格式.普通建筑姿态):
                姿态警告()

    def 转比特流(self) -> bytes:
        self.检查姿态()
        流数据 = bytearray()
        # V0.10.34.28281: 版本标识改为-102
        流数据.extend(struct.pack("<i", -102))
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
                self.配方序号.转int(),
                self.过滤物品序号.转int(),
            )
        )
        流数据.extend(self.额外参数.转比特流())
        
        # V0.10.34.28281: 额外文本内容（先 Int32 字符数，再 7-bit 字节长度 + UTF-8 字节，与游戏一致）
        content_bytes = self.额外文本内容.encode('utf-8')
        byte_len = len(content_bytes)
        if byte_len == 0:
            流数据.extend(struct.pack("<i", 0))
        else:
            流数据.extend(struct.pack("<i", len(self.额外文本内容)))
            content_length = byte_len
            while content_length >= 0x80:
                流数据.extend(struct.pack("B", (content_length & 0x7F) | 0x80))
                content_length >>= 7
            流数据.extend(struct.pack("B", content_length & 0x7F))
            流数据.extend(content_bytes)
        
        return 流数据
    # 转比特流 到此为止


    def 转json(self):
        返回值 = self.原始函数_转json()
        if self.模型序号.是传送带吗() or self.模型序号.是分拣器吗():
            return 返回值
        # 创建新字典，按原始顺序重建键
        新返回值 = {}
        for 键值 in 返回值.keys():
            if 键值 == '输入接口':
                新返回值['堆叠接口'] = 返回值[键值]
            else:
                新返回值[键值] = 返回值[键值]
        return 新返回值
    @classmethod
    def 由json转换(cls, 数据字典: dict):
        数据字典 = dict(数据字典)
        if '堆叠接口' in 数据字典:
            数据字典['输入接口'] = 数据字典.pop('堆叠接口')
        if '额外文本解析' in 数据字典:
            数据字典['额外文本内容'] = 由额外文本解析组合(数据字典.pop('额外文本解析'))
        return cls.原始函数_由json转换(数据字典)


# 建筑 到此为止
