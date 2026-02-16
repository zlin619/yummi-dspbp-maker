from 功能.虚空之遗.虚空之遗全流程 import 虚空之遗
from 应用.版本修正 import 版本修正
from 文件.文件读写 import 保存蓝图, 工程目录, 读取泛蓝图文件, 建筑蓝图目录, 保存所有建筑
from 功能.舍弃精度 import 批量舍弃精度
from 功能.指鹿为马.改天换地 import 改天换地
from 功能.指鹿为马.通用 import 强制纠正姿态
from 功能.接口简单分析 import 尝试接口分析
import shutil
import os

from 蓝图格式.图标 import 图标
from 蓝图格式.蓝图 import 蓝图




print("脚本运行开始")


source_dir = R"C:\Users\Admin\Documents\Dyson Sphere Program\Blueprint\猫猫修仙\仙术模板\仙术换模黑台"
target_dir = R"C:\Users\Admin\Documents\Dyson Sphere Program\Blueprint\猫猫修仙\仙术模板\仙术换模黑带带爪"
基本蓝图: 蓝图 = 读取泛蓝图文件(Rf"{工程目录()}\蓝图库\临时\输入蓝图.json")

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)

# 遍历源目录中的所有txt文件并复制到目标目录
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename+".json")

        母本蓝图 = 读取泛蓝图文件(source_path)
        基本蓝图.蓝图头部 = 母本蓝图.蓝图头部
        基本蓝图.蓝图中段.建筑[0].物品序号 = 母本蓝图.蓝图中段.建筑[0].物品序号
        基本蓝图.蓝图中段.建筑[0].模型序号 = 母本蓝图.蓝图中段.建筑[0].模型序号
        基本蓝图.蓝图中段.建筑[0].配方序号 = 母本蓝图.蓝图中段.建筑[0].配方序号
        强制纠正姿态(基本蓝图)
        保存蓝图(基本蓝图).为蓝图txt文件(target_path)
        保存蓝图(基本蓝图).为json文件(target_path)



print("脚本运行结束")