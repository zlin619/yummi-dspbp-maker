from 蓝图格式.中段 import 蓝图中段
from 蓝图格式.蓝图 import 蓝图
from 蓝图格式.区域 import 区域

# 把蓝图的区域和锚点归到 1 * 1
# 这个功能可以让蓝图可以跨纬度铺设
# 但由此产生的蓝图在跨纬度时更容易碰撞

def _确保区域唯一(所有区域: list[区域]):
    if len(所有区域) != 1:
        raise ValueError(f"区域数{len(所有区域)}不为1, 不可删除锚点。输入的list必须只包含1个区域。")
    if not isinstance(所有区域[0], 区域):
        raise TypeError(f"输入的list的首个元素不是区域。输入的list必须只包含1个区域。")
    return 所有区域[0]

def _单锚点(本区域: 区域):
    本区域.大小.东西X = 1
    本区域.大小.南北Y = 1

def 转换为单锚点(输入数据) -> 区域:
    # 修改区域为新区域，并返回新区域
    if isinstance(输入数据, 蓝图):
        return 转换为单锚点(输入数据.蓝图中段.区域)
    elif isinstance(输入数据, 蓝图中段):
        return 转换为单锚点(输入数据.区域)
    elif isinstance(输入数据, list):
        旧区域 = _确保区域唯一(输入数据)
        return 转换为单锚点(旧区域)
    elif isinstance(输入数据, 区域):
        return _单锚点(输入数据)
    else:
        raise TypeError(f"输入{输入数据.__class__}必须是 蓝图、蓝图中段、区域列表 或 单个区域。")
