from 功能.平移缩放 import 平移缩放
from 功能.浮空地基 import 添加仙术地基
from 功能.虚空之遗.点对点带对带 import 点对点带对带重连
from 功能.虚空之遗.虚空之遗全流程 import 虚空之遗
from 应用.版本修正 import 版本修正
from 文件.文件读写 import 保存蓝图, 工程目录, 读取泛蓝图文件, 建筑蓝图目录, 保存所有建筑
from 功能.舍弃精度 import 批量舍弃精度
from 功能.指鹿为马.改天换地 import 改天换地
from 功能.指鹿为马.通用 import 强制纠正姿态
from 功能.接口简单分析 import 尝试接口分析
from 蓝图格式.坐标 import 空间坐标
import tkinter as tk

def copy_to_clipboard(text):
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()
# 这个文件的主要作用是让人知道悠米是怎么喵的X
# 这个文件的主要作用是让人知道悠米是最近拿蓝图工具主要在整什么活的
# 在命令行输入   python -m 应用.悠米悠米   即可
# 这个文件夹里的文件，每一个都可以当主函数运行。

print("脚本运行开始")

本蓝图 = 读取泛蓝图文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图.json")
版本修正(本蓝图)
#强制纠正姿态(本蓝图)
#批量舍弃精度(本蓝图).旋转().坐标()
#平移缩放(本蓝图).建筑平移(空间坐标(0, 0 ,40))
#添加仙术地基(本蓝图)
改天换地(本蓝图)

#尝试接口分析(本蓝图)
#虚空之遗(本蓝图)
#点对点带对带重连(本蓝图)
#添加仙术地基(本蓝图)
保存蓝图(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图.json")
保存蓝图(本蓝图).为蓝图txt文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图.txt")
保存所有建筑(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出所有建筑.json")
保存蓝图(本蓝图).为蓝图txt文件(Rf"{建筑蓝图目录()}\生成蓝图\生成蓝图.txt")
# 复制到剪贴板
copy_to_clipboard(本蓝图.转蓝图字符串())

print("脚本运行结束")
