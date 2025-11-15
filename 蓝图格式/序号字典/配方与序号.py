from typing import Dict
# 用法: from 蓝图格式.序号字典.模型与序号 import 序号转模型, 模型转序号

# 正向映射
序号转配方: Dict[int, str] = {
    0: '无配方',
}


# 反向映射
配方转序号: Dict[str, int] = {
    '无配方': 0,
    '未定义': 0,
}
