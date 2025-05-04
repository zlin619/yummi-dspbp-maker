from 文件.蓝图文件解析.解析 import 解析
from dataclasses import dataclass, asdict
from 蓝图格式.模型 import 模型
from 蓝图格式.蓝图 import *
from 蓝图格式.坐标 import *
from 蓝图格式.中段 import *
import json
from 文件.通用 import *

参考蓝图 = """
BLUEPRINT:0,10,2001,0,0,0,0,0,638758399039585557,0.10.32.25699,%E4%B8%80%E4%B8%AA%E4%BC%A0%E9%80%81%E5%B8%A6,%E6%99%AE%E6%99%AE%E9%80%9A%E9%80%9A%2C%E6%AF%AB%E6%97%A0%E4%BD%9C%E7%94%A8"H4sIAAAAAAAAC2NkQAWMUAxh/2dgOAFlMoKFZ////x/Ev8iujKRngqQ5A4OJM4j9HwqQjGEAADRnUB9kAAAA"147F66CC116DC8FB07887AC4836777DF
"""

预期结果 = """
{"header":{"layout":10,"icons":[2001,0,0,0,0],"time":"2025-02-22T16:51:43.958Z","gameVersion":"0.10.32.25699","shortDesc":"一个传送带","desc":"普普通通,毫无作用"},"version":1,"cursorOffset":{"x":0,"y":0},"cursorTargetArea":0,"dragBoxSize":{"x":1,"y":1},"primaryAreaIdx":0,"areas":[{"index":0,"parentIndex":-1,"tropicAnchor":0,"areaSegments":200,"anchorLocalOffset":{"x":0,"y":0},"size":{"x":1,"y":1}}],"buildings":[{"parameters":null,"index":0,"itemId":2001,"modelIndex":35,"areaIndex":0,"localOffset":[{"x":0,"y":0,"z":0},{"x":0,"y":0,"z":0}],"yaw":[180,180],"tilt":0,"pitch":0,"tilt2":0,"pitch2":0,"outputObjIdx":-1,"inputObjIdx":-1,"outputToSlot":0,"inputFromSlot":0,"outputFromSlot":0,"inputToSlot":1,"outputOffset":0,"inputOffset":0,"recipeId":0,"filterId":0,"itemName":"传送带"}]}
"""

未知蓝图="""
BLUEPRINT:0,10,6001,0,0,0,0,0,638725880353110111,0.10.31.24710,240%E8%93%9D%E7%B3%96,"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"1E3A71CB34D03DEA880E592FD2742706
"""

字符串 = r"""
H4sIAAAAAAAAC2NkQAWMUAxh/2dgOAFlMoKFZ////x/Ev8iujKRngqQ5A4OJM4j9HwqQjGEAADRnUB9kAAAA
"""
#蓝图 = 解析(未知蓝图.strip())


#print(蓝图.转蓝图字符串())
#print(asdict(蓝图.蓝图中段))


#保存文件(R"E:\developing\悠米蓝图工具alpha0.2\临时\临时.json", 蓝图.转json())
js21321 = 读取文件(Rf"{工程目录()}\临时\输入.json")

local_蓝图 = 蓝图(**js21321)
print(local_蓝图.蓝图中段.__class__)

保存文件(Rf"{工程目录()}\临时\输出.json", local_蓝图.蓝图中段.建筑.转json())
#from dataclasses import dataclass, fields
#def flat_as_dict(obj) -> dict:
#    return {field.name: getattr(obj, field.name) for field in fields(obj)}

#field_names = [field.name for field in fields(蓝图.蓝图中段)]
#print(field_names)

#print(flat_as_dict(蓝图.蓝图中段).keys())


# 设计一个基类
# 可以递归执行 json输出

import time
timeArray = time.localtime(timeStamp)

# 将本地时间格式化为指定的格式
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
