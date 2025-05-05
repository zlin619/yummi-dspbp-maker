from dataclasses import dataclass
from dataclasses import fields
from typing import Annotated, get_origin, get_args, Type, Any
from enum import Enum, IntEnum

class 布尔值(IntEnum):
    否 = 0
    是 = 1

class _字典转换器:
    # 尽可能不要使用这个类
    @staticmethod
    def 转换字段值(字段类型: Type, 字段值: Any) -> dict | list:
        原始字段 = get_origin(字段类型)
        if 原始字段 is Annotated:
            真实类型 = get_args(字段类型)[0]  # 提取int部分
            return _字典转换器.转换字段值(真实类型, 字段值)  # 递归处理
        elif 原始字段 is list:
            元素类型 = get_args(字段类型)[0]
            return [_字典转换器.转换字段值(元素类型, x) for x in 字段值]
        elif issubclass(字段类型, Enum):
            return 字段类型[字段值]
        elif issubclass(字段类型, 蓝图基类):
            return 字段类型.由json转换(字段值)
        else:
            return 字段值

    @staticmethod
    def 收集字段数据(目标类: Type, 源字典: dict) -> dict:
        return {
            field.name: _字典转换器.转换字段值(field.type, 源字典[field.name])
            for field in fields(目标类)
        }

    @classmethod
    def 转换为class(cls, 目标类: Type, 源字典: dict) -> Any:
        return 目标类(**cls.收集字段数据(目标类, 源字典))


@dataclass
class 蓝图基类:
    def 转json(self):
        raise NotImplementedError(f"谢谢你，这个算虚基类方法，请重写方法。类名：{self.__class__}")

    @classmethod
    def 由json转换(cls, 数据字典: dict):
        raise NotImplementedError(f"谢谢你，这个算虚基类方法，请重写方法。类名：{cls}")


@dataclass
class 蓝图dataclass基类(蓝图基类):
    def 转json(self):
        结果 = {}
        for field in fields(self):
            if field.name.startswith('_'):  # 跳过私有字段
                continue
            value = getattr(self, field.name)
            if issubclass(type(value), 蓝图基类):
                结果[field.name] = value.转json()
            elif isinstance(value, list):
                结果[field.name] = [item.转json() if isinstance(item, 蓝图基类) else item for item in value]
            elif isinstance(value, IntEnum):
                结果[field.name] = value.name
            else:
                结果[field.name] = value
        return 结果

    @classmethod
    def 由json转换(cls, 数据字典: dict):
        return _字典转换器.转换为class(cls, 数据字典)


def 由json转换为类型(类型, 数据字典: dict):
    return _字典转换器.转换为class(类型, 数据字典)


def 由json列表转换为类型列表(子类型, 列表: list):
    新列表 = []
    for 小字典 in 列表:
        类 = _字典转换器.转换为class(子类型, 小字典)
        新列表.append(类)
    return 新列表
