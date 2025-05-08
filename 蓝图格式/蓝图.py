from dataclasses import dataclass
from datetime import datetime
from typing import Union
from urllib.parse import unquote, quote

from 文件.签名 import 签名的蓝图
from 蓝图格式.中段 import 蓝图中段
from 蓝图格式.图标 import 图标
from 蓝图格式.蓝图基础类型 import 蓝图基类, 蓝图dataclass基类


class 时间戳(蓝图基类):
    DotNet时间戳: int

    # 输入为DateTime.Ticks。根据微软文档：
    # The value of this property represents the number of 100-nanosecond intervals that have elapsed since 12:00:00 midnight, January 1, 0001 in the Gregorian calendar
    # 因此我们命名100ns为1 tick
    # datetime用的是POSIX时间戳, 是1970年01月01日00时00分00秒 起至现在的总秒数
    def __init__(self, 时间输入: Union[int, str]):
        if isinstance(时间输入, int):
            self.DotNet时间戳 = 时间输入
        elif isinstance(时间输入, str):
            self.DotNet时间戳 = self.时间转整数(时间输入)
        else:
            raise TypeError("输入类型必须是int或str")

    @staticmethod
    def 整数转时间(时间戳数字: int) -> str:
        unix_ticks = 时间戳数字 - 621355968 * 1e9
        POSIX时间戳 = unix_ticks / 1e7
        return str(datetime.fromtimestamp(POSIX时间戳))

    @staticmethod
    def 时间转整数(时间字符串: str) -> int:
        try:
            unix_ticks = datetime.strptime(时间字符串, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1e7
            return int(unix_ticks + 621355968 * 1e9)
        except ValueError:
            raise ValueError("时间戳格式错误。请使用ISO 8601格式。")

    def 转json(self) -> str:
        return 时间戳.整数转时间(self.DotNet时间戳)

    @classmethod
    def 由json转换(cls, 数据字典):
        return 时间戳(时间戳.时间转整数(数据字典))

    def 转蓝图字符串(self) -> str:
        return str(self.DotNet时间戳)


class url字符串(蓝图基类):
    自然字符串: str

    def __init__(self, 输入):
        self.自然字符串 = 输入

    def __repr__(self):
        return self.自然字符串

    @staticmethod
    def 转自然字符串(url: str) -> str:
        return unquote(url)

    @staticmethod
    def 转url字符串(自然字符串: str) -> str:
        return quote(自然字符串)

    def 转json(self) -> str:
        return self.自然字符串

    @classmethod
    def 由json转换(cls, 输入字符串):
        return url字符串(输入字符串)

    @staticmethod
    def 从url构造(url: str) -> str:
        return url字符串(url字符串.转自然字符串(url))

    def 转蓝图字符串(self):
        return self.转url字符串(self.自然字符串)


@dataclass
class 缩略图(蓝图dataclass基类):
    图标布局: int
    图标1: 图标
    图标2: 图标
    图标3: 图标
    图标4: 图标
    图标5: 图标
    小标题: url字符串
    ########################
    # 以上为字段，以下为函数 #
    ########################


# 缩略图 到此为止


@dataclass
class 蓝图头部(蓝图dataclass基类):
    缩略图: 缩略图
    创建时间: 时间戳
    游戏版本: str
    蓝图描述: url字符串

    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转蓝图字符串(self) -> str:
        return ','.join([
            '0',  # 固定值
            str(self.缩略图.图标布局),
            self.缩略图.图标1.转蓝图字符串(),
            self.缩略图.图标2.转蓝图字符串(),
            self.缩略图.图标3.转蓝图字符串(),
            self.缩略图.图标4.转蓝图字符串(),
            self.缩略图.图标5.转蓝图字符串(),
            '0',  # 固定值
            self.创建时间.转蓝图字符串(),
            self.游戏版本,
            self.缩略图.小标题.转蓝图字符串(),
            self.蓝图描述.转蓝图字符串()
        ])


# 蓝图头部 到此为止


@dataclass
class 蓝图(蓝图dataclass基类):
    蓝图头部: 蓝图头部
    蓝图中段: 蓝图中段

    ########################
    # 以上为字段，以下为函数 #
    ########################
    def 转蓝图字符串(self) -> str:
        签名前蓝图 = 'BLUEPRINT:{}"{}'.format(
            self.蓝图头部.转蓝图字符串(),
            self.蓝图中段.转蓝图字符串()
        )
        return 签名的蓝图(签名前蓝图)

    # def 解析(原始蓝图: str) -> 蓝图:
    # 这个函数在解析.py里

# 蓝图 到此为止
