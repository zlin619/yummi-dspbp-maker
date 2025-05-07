from enum import Enum, auto

class mod类型(Enum):
    戴森球原版 = auto()
    创世之书30 = auto()
    创世之书31 = auto()
    宇宙创生 = auto()

_当前_mod类型 = mod类型.戴森球原版

def 当前mod类型():
    global _当前_mod类型
    return _当前_mod类型

def 设置mod类型(l_mod类型):
    global _当前_mod类型
    if not isinstance(l_mod类型, mod类型):
        raise ValueError("参数必须是Mod类型枚举值")
    _当前_mod类型 = l_mod类型
