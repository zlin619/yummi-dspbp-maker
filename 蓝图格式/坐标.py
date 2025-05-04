import struct
from dataclasses import dataclass
from 蓝图格式.蓝图基础类型 import *
import 蓝图格式.类型 as 类型

class 姿态(蓝图dataclass基类):
    # 伪纯虚基类
    def 转比特流(self) -> bytes:
        raise NotImplementedError("伪纯虚基类，还想执行方法，想屁吃？")
    
    @classmethod
    def 由json转换为cls(cls, 数据字典):
        if 数据字典["姿态类型"] == "全空间姿态":
            return 全空间姿态.由json转换为cls(数据字典)
        elif 数据字典["姿态类型"] == "传送带姿态":
            return 传送带姿态.由json转换为cls(数据字典)
        elif 数据字典["姿态类型"] == "普通建筑姿态":
            return 普通建筑姿态.由json转换为cls(数据字典)
        elif 数据字典["姿态类型"] == "分拣器姿态":
            return 分拣器姿态.由json转换为cls(数据字典)
        else:
            raise NotImplementedError("伪纯虚基类，还想执行方法，想屁吃？")

@dataclass
class 全空间姿态(姿态):
    东西X: float
    南北Y: float
    高度Z: float
    水平旋转Z: float
    左右倾斜X: float # 爪带独有
    上下翻滚Y: float # 分拣器独有
    姿态类型: str = "全空间姿态"
    # 注: 分拣器拥有2种姿态,起点和终点
    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转比特流(self) -> bytes:
        return struct.pack(
            "<6f",
            self.东西X,
            self.南北Y,
            self.高度Z,
            self.水平旋转Z,
            self.左右倾斜X,
            self.上下翻滚Y
        )

    @classmethod
    def 由json转换为cls(cls, 数据字典):
        return 全空间姿态(**数据字典)
# 全空间姿态 到此为止

@dataclass
class 传送带姿态(姿态):
    东西X: float
    南北Y: float
    高度Z: float
    水平旋转Z: float
    左右倾斜X: float # 爪带独有
    姿态类型: str = "传送带姿态"
    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转比特流(self) -> bytes:
        return struct.pack(
            "<5f",
            self.东西X,
            self.南北Y,
            self.高度Z,
            self.水平旋转Z,
            self.左右倾斜X
        )
    
    @classmethod
    def 由json转换为cls(cls, 数据字典):
        return 传送带姿态(**数据字典)
# 传送带姿态 到此为止

@dataclass
class 普通建筑姿态(姿态):
    东西X: float
    南北Y: float
    高度Z: float
    水平旋转Z: float
    姿态类型: str = "普通建筑姿态"
    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转比特流(self) -> bytes:
        return struct.pack(
            "<4f",
            self.东西X,
            self.南北Y,
            self.高度Z,
            self.水平旋转Z
        )
    
    @classmethod
    def 由json转换为cls(cls, 数据字典):
        return 普通建筑姿态(**数据字典)
# 普通建筑姿态 到此为止

@dataclass
class 分拣器姿态(姿态):
    起点: 全空间姿态
    终点: 全空间姿态
    姿态类型: str = "分拣器姿态"
    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转比特流(self) -> bytes:
        return self.起点.转比特流() + self.终点.转比特流()
    
    @classmethod
    def 由json转换为cls(cls, 数据字典):
        return 分拣器姿态(
            起点 = 全空间姿态.由json转换为cls(数据字典["起点"]),
            终点 = 全空间姿态.由json转换为cls(数据字典["终点"])
        )
# 分拣器姿态 到此为止


@dataclass
class 空间坐标(蓝图dataclass基类):
    东西X: float
    南北Y: float
    高度Z: float

@dataclass
class 平面坐标(蓝图dataclass基类):
    东西X: float
    南北Y: float

@dataclass
class Int16平面坐标(蓝图dataclass基类):
    东西X: 类型.Int16
    南北Y: 类型.Int16

@dataclass
class Int32平面坐标(蓝图dataclass基类):
    东西X: 类型.Int32
    南北Y: 类型.Int32

# 横为东西 纵为南北

