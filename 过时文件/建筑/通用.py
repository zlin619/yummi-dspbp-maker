import 日志
日志.正在加载("建筑 通用")


def 是分拣器吗(building):
    return building.get('modelIndex') in [41, 42, 43, 483]

def 是传送带吗(building):
    return building.get('modelIndex') in [35, 36, 37]

def 是塔吗(building):
    return building.get('modelIndex') in [49, 50]

def 是带图标的传送带吗(building):
    # 这个逻辑在无带流和CE蓝图很重要
    return building.get('modelIndex') in [35, 36, 37] and building['parameters']

def 是虚拟物品吗(building):
    # 如果建筑为铁，通常表示悠米打算废弃这个建筑。但悠米懒得处理，很麻烦。
    # 如果建筑为铁，通常表示晨隐的蓝图工具做了地基堆叠仙术。
    return building.get('itemId') == 1001 or building.get('itemId') == 1131

日志.加载完成("建筑 通用")