
from 文件.蓝图文件解析.解析中段 import 解析中段
from 文件.蓝图文件解析.解析头部 import 解析头部
from 蓝图格式.蓝图 import 蓝图

def 分割字符(原始蓝图: str) -> tuple[str, str]:
    蓝图 = 原始蓝图.strip()
    if not 蓝图.startswith('BLUEPRINT:'):
        raise ValueError('蓝图格式错误: 蓝图文件必须以"以BLUEPRINT:"打头')
    # BLUEPRINT:[头部]"Base64蓝图核心"[尾部MD5校验]
    # 提取头部 核心 尾部, 按"分割

    # 去掉前缀 'BLUEPRINT:'
    蓝图 = 蓝图.split('BLUEPRINT:')[1]

    # 按双引号分割字符串
    分割蓝图 = 蓝图.split('"')
    if len(分割蓝图) != 3:
        raise ValueError('蓝图格式错误: 分割异常, 蓝图文件应该被2个双引号"分割成3段')
    头部字符 = 分割蓝图[0]
    中段字符 = 分割蓝图[1]
    # 尾部字符 = 分割蓝图[2] #md5校验 可以舍弃
    return 头部字符, 中段字符

def 将原始蓝图文件字符串解析为蓝图(原始蓝图文件字符串: str) -> 蓝图:
    头部字符, 中段字符 = 分割字符(原始蓝图文件字符串)
    头部 = 解析头部(头部字符)
    中段 = 解析中段(中段字符)
    return 蓝图(蓝图头部=头部, 蓝图中段=中段)

