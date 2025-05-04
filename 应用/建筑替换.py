from dataclasses import dataclass, asdict
from 蓝图格式.蓝图 import *
from 文件.文件读写 import *

# 这个文件的主要作用是做给0代码基础的人看看
# 首先, 你要下载VSCode和Python
# VSCode语言改成中文: https://soft.3dmgame.com/gl/1012.html
# VSCode无视中文黄框: https://blog.csdn.net/qq_36972930/article/details/145533116
# 以VSCode打开整个 悠米蓝图工具 文件夹
# 左上角, 终端(R), 新建终端
# 在命令行输入   python -m 应用.简单转换   即可
# 作用是把输入.txt 转换为2个输出。
# 输入做了优化，Json文件就按Json读取，蓝图文件就按蓝图读取。

# 最后，这个文件夹里的文件，每一个都可以当主函数运行。

本蓝图   = 读取txt文件(Rf"{工程目录()}\蓝图库\临时\输入蓝图.txt").转换为蓝图()
所有建筑 = 读取json文件(Rf"{工程目录()}\蓝图库\临时\输入所有建筑.json").转换为所有建筑()
本蓝图.蓝图中段.建筑 = 所有建筑
保存蓝图(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图.json")
