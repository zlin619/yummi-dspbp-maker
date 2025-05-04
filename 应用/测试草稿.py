
from dataclasses import dataclass, asdict
from 蓝图格式.模型 import 模型
from 蓝图格式.蓝图 import *
from 蓝图格式.坐标 import *
from 蓝图格式.中段 import *
from 文件.文件读写 import *
from 文件.蓝图文件解析.解析 import 读取泛蓝图文件

# python -m 应用.测试草稿

本蓝图 = 读取泛蓝图文件(Rf"{工程目录()}\临时\输入.txt")
保存json文件(Rf"{工程目录()}\临时\输出1.json", 本蓝图)
保存txt蓝图文件(Rf"{工程目录()}\临时\输出1.txt", 本蓝图)

本蓝图 = 读取泛蓝图文件(Rf"{工程目录()}\临时\输入.json")
保存json文件(Rf"{工程目录()}\临时\输出2.json", 本蓝图)
保存txt蓝图文件(Rf"{工程目录()}\临时\输出2.txt", 本蓝图)
