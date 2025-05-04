import json

from 文件.蓝图文件解析.解析 import 将原始蓝图文件字符串解析为蓝图
from 蓝图格式.中段 import 蓝图中段
from 蓝图格式.建筑 import 建筑
from 蓝图格式.蓝图 import 蓝图
from 蓝图格式.蓝图基础类型 import 由json列表转换为类型列表
from 蓝图格式.蓝图基础类型 import 由json转换为类型


# 用法: 本蓝图 = 读取txt文件(R"E:\蓝图文件夹\临时蓝图.txt").转换为蓝图()
class 读取txt文件:
    def __init__(self, 文件路径: str):
        with open(文件路径, 'r', encoding='utf-8') as 文件:
            self.文本 = 文件.read()

    def 转换为文本(self) -> str:
        return self.文本

    def 转换为蓝图(self) -> 蓝图:
        return 将原始蓝图文件字符串解析为蓝图(self.文本)


# 用法: 本蓝图 = 读取json文件(R"E:\蓝图文件夹\临时蓝图.json").转换为蓝图()
class 读取json文件:
    def __init__(self, 文件路径: str):
        with open(文件路径, 'r', encoding='utf-8') as 文件:
            self.json数据 = json.load(文件)

    def 转换为字典(self) -> dict:
        return self.json数据

    def 转换为蓝图(self) -> 蓝图:
        return 由json转换为类型(蓝图, self.json数据)

    def 转换为所有建筑(self) -> list:
        return 由json列表转换为类型列表(建筑, self.json数据)


# 用法: 保存蓝图(当前蓝图).为json文件(R"E:\蓝图文件夹")
class 保存蓝图:
    def __init__(self, 输入):
        if isinstance(输入, 蓝图):
            self.本蓝图 = 输入
        else:
            raise TypeError("输入的不是蓝图")

    def 为蓝图txt文件(self, 文件路径: str) -> None:
        with open(文件路径, 'w', encoding='utf-8') as 文件:
            文件.write(self.本蓝图.转蓝图字符串())

    def 为json文件(self, 文件路径: str) -> None:
        with open(文件路径, 'w', encoding='utf-8') as 文件:
            json.dump(self.本蓝图.转json(), 文件, ensure_ascii=False, indent=4)


# 用法: 保存蓝图(输入).为json文件(R"E:\蓝图文件夹")
# 输入必须是 蓝图、蓝图中段、所有建筑中的一个
class 保存所有建筑:
    def __init__(self, 输入):
        if isinstance(输入, 蓝图):
            self.所有建筑 = 输入.蓝图中段.转json()["建筑"]
        elif isinstance(输入, 蓝图中段):
            self.所有建筑 = 输入.转json()["建筑"]
        elif isinstance(输入, list):
            self.所有建筑 = 输入
        else:
            raise TypeError(f"输入{输入.__class__}必须是 蓝图、蓝图中段、所有建筑中的一个。")

    def 为json文件(self, 文件路径: str) -> None:
        with open(文件路径, 'w', encoding='utf-8') as 文件:
            json.dump(self.所有建筑, 文件, ensure_ascii=False, indent=4)


def 读取泛蓝图文本(文本: str) -> 蓝图:
    文本 = 文本.strip()
    if 文本.startswith("BLUEPRINT:"):
        return 将原始蓝图文件字符串解析为蓝图(文本)
    elif 文本.startswith("{"):
        json数据 = json.loads(文本)
        return 由json转换为类型(蓝图, json数据)
    else:
        raise ValueError("文本内容必须以'BLUEPRINT:'或'{'开头")


def 读取泛蓝图文件(文件路径: str) -> 蓝图:
    return 读取泛蓝图文本(读取txt文件(文件路径).转换为文本())


def 工程目录() -> str:
    return __file__.split("文件")[0]
