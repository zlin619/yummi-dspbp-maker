import base64
import gzip
import struct
from dataclasses import dataclass

from 蓝图格式.中段杂项 import 中段杂项
from 蓝图格式.区域 import 区域
from 蓝图格式.建筑 import 建筑
from 蓝图格式.蓝图基础类型 import 蓝图dataclass基类


def Base64压缩(Base64字符) -> str:
    压缩数据 = gzip.compress(Base64字符)
    Base64字符 = base64.b64encode(压缩数据).decode('utf-8')
    return Base64字符


@dataclass
class 蓝图中段(蓝图dataclass基类):
    杂项: 中段杂项
    区域: list[区域]
    建筑: list[建筑]

    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转比特流(self) -> bytes:
        流数据 = bytearray()
        流数据.extend(self.杂项.转比特流())
        流数据.extend(struct.pack("b", len(self.区域)))
        for 单个区域 in self.区域:
            流数据.extend(单个区域.转比特流())
        流数据.extend(struct.pack("i", len(self.建筑)))
        for 单个建筑 in self.建筑:
            流数据.extend(单个建筑.转比特流())
        return bytes(流数据)

    def 转蓝图字符串(self) -> str:
        流数据 = self.转比特流()
        return Base64压缩(流数据)
# 蓝图中段 到此为止
