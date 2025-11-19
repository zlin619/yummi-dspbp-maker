from copy import deepcopy
from 功能.基站修正 import 修正基站供电
from 功能.平移缩放 import 平移缩放
from 功能.浮空地基 import 添加仙术地基
from 功能.百倍矿机 import 替换为百倍大矿机
from 功能.虚空之遗.点对点带对带 import 点对点带对带重连
from 功能.虚空之遗.虚空之遗全流程 import 虚空之遗
from 应用.版本修正 import 版本修正
from 文件.文件读写 import 保存蓝图, 工程目录, 读取泛蓝图文件, 建筑蓝图目录, 保存所有建筑, 读取泛蓝图文本
from 功能.舍弃精度 import 批量舍弃精度
from 功能.指鹿为马.改天换地 import 改天换地
from 功能.指鹿为马.通用 import 强制纠正姿态
from 功能.接口简单分析 import 尝试接口分析
from 蓝图格式 import 类型
from 蓝图格式.图标 import 图标
from 蓝图格式.坐标 import 全空间姿态, 分拣器姿态, 空间坐标
import pyperclip

from 蓝图格式.建筑 import 建筑, 建筑主导接口, 建筑类型分析
from 蓝图格式.接口分析.多接口分析 import 多接口分析
from 蓝图格式.模型 import 模型
from 蓝图格式.蓝图基础类型 import 布尔值
from 蓝图格式.配方 import 配方
from 蓝图格式.额外参数 import 额外参数之传送带, 额外参数之制造类建筑

# 这个文件的主要作用是让人知道悠米是怎么喵的X
# 这个文件的主要作用是让人知道悠米是最近拿蓝图工具主要在整什么活的
# 在命令行输入   python -m 应用.悠米悠米   即可
# 这个文件夹里的文件，每一个都可以当主函数运行。


def 生成仙爪黑炉(序号: int, x: float, y: float, z: float, 输入配方 = 配方("未定义")) -> 建筑:
    子姿态 = 全空间姿态(
        东西X=x,
        南北Y=y,
        高度Z=z,
        水平旋转Z=0.0,
        左右倾斜X=0.0,
        上下翻滚Y=0.0,
    )
    全姿态 = 分拣器姿态(
        起点=deepcopy(子姿态),
        终点=deepcopy(子姿态),
    )

    输出接口 = 建筑主导接口(
        目标序号=类型.Int32(-1),
        目标接口=类型.Int8(0),
        自身接口=类型.Int8(0),
        插槽偏移=类型.Int8(0)
    )
    输入接口 = 建筑主导接口(
        目标序号=类型.Int32(-1),
        目标接口=类型.Int8(0),
        自身接口=类型.Int8(0),
        插槽偏移=类型.Int8(0)
    )
    return 建筑(
        建筑序号=序号,
        区域序号=0,
        物品序号=图标("分拣器"),
        模型序号=模型("负熵熔炉"),
        空间姿态=全姿态,

        输出接口=输出接口,
        输入接口=输入接口,
        配方序号=输入配方,
        过滤物品序号=图标("未定义"),
        额外参数=额外参数之制造类建筑(
            是否生产加速=布尔值.是,
        ),

        悠米_接口分析 = 多接口分析(),
        悠米_建筑类型 = 建筑类型分析.无特殊性,
    )


print("脚本运行开始")

本蓝图 = 读取泛蓝图文本('''
BLUEPRINT:0,10,0,0,0,0,0,0,638990098192137356,0.10.33.27026,%E6%96%B0%E8%93%9D%E5%9B%BE,"H4sIAAAAAAAACmNiYGBgBGImBghgBmJWKJuR4T8DwwmoMCsDL5Ce/f//fxD/HvtjRoaTSwLtrlvPsj84021X2D9j520dk+zqT4bYrXwdaPdcQcX84Ez5XTX/jZ0XSGXY5hs+teEGauQB4v8cDIy/oTYwQg1lhBkqKBRoJ8E5weHgTOdd8b+MnbvffbPaOnO6rWJKoB3fAyMHkGWCf42dC4GWpT/d7AwykAtk1n+gWUBTfVkYwZ4BGcoEM3TN3af2rNwQQ+0ZTZw1TE/uMvq22Tnr8lN7mKEfmEyc425vdoYZCgoJJpChLKiGgsQvs6syMBRxMjhc4ZrgwHhAcpsoY7szAzTo/kO8wwgNRbAmFphL3L7U24M0NRqf3XkL6A2br5ud6xbYbDv+v97e4aGRQ+Eynd0MDCbOMUKSZjCXgAxl/A8xcCOSS1hhLgkTbbC/CHXJi39tYJdw4XAJG8wlIBsn2c6yB9nIBLRR80ms6T9g7HEzNNibL68Fxp7Drv/A2BOW7bWasLfJjB0We+wgx6DGHjvMJSBDV6nPNwG5hIEBEibcOFzCAdP0/v9/e7B5EyTN86Ga2HFo4oQ5n+30U/ur0MS3lhESdSnHQ+wcDj+1hyW+BqC3Jvzc7Jz9Z7MzB8z5bAyMLGjO54K55PQBa6t0DkhAHvoDCcj/UMCA5hJumCagf7fBnD/xP35NIBfwc56EhD5QxgESUCga4LkPTgIAKsA4J6UDAAA="39B500AF4CB7B8FEF9B076A068C17254
''')

版本修正(本蓝图)

本蓝图.蓝图中段.建筑 = []
本蓝图.蓝图中段.建筑.append(
    生成仙爪黑炉(
        序号=0,
        x=0.0,
        y=0.0,
        z=0.0,
        输入配方=配方("铁板"),
    )
)
平移缩放(本蓝图).建筑平移(空间坐标(0, 0, 8.75))



#强制纠正姿态(本蓝图)
批量舍弃精度(本蓝图).旋转().坐标()
#平移缩放(本蓝图).建筑平移(空间坐标(0, 0 ,40))
#添加仙术地基(本蓝图)
#改天换地(本蓝图)

#尝试接口分析(本蓝图)
#虚空之遗(本蓝图)
#点对点带对带重连(本蓝图)
#添加仙术地基(本蓝图)




#替换为百倍大矿机(本蓝图)
#修正基站供电(本蓝图)
#强制纠正姿态(本蓝图)
#尝试接口分析(本蓝图)


#点对点带对带重连(本蓝图)
#强制纠正姿态(本蓝图)
#尝试接口分析(本蓝图)
保存蓝图(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图.json")
#保存蓝图(本蓝图).为蓝图txt文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图.txt")
#保存所有建筑(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出所有建筑.json")
#保存蓝图(本蓝图).为蓝图txt文件(Rf"{建筑蓝图目录()}\生成蓝图\生成蓝图.txt")
# 复制到剪贴板
pyperclip.copy(本蓝图.转蓝图字符串())
print("脚本运行结束")
