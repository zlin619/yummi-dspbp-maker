import json
from pathlib import Path
from pprint import pformat

def 文件头部注释与导入() -> str:
    return f"""
# 请不要修改这个文件
# 这个文件由 原序号字典下的几个py构建而成
# 自动生成时间：{__import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

from typing import Dict
""".strip()

def 字典转文本(输入字典: dict) -> str:
    内容 = pformat(输入字典, width=200, indent=4)
    内容 = 内容.replace("{", " ").replace("}", "")
    return f"{{\n{内容}\n}}\n"

def 蓝图格式目录() -> str:
    return __file__.split("蓝图格式")[0] + "蓝图格式"

json路径 = Path(蓝图格式目录()) / "原序号字典" / "创世之书31" / "创世之书.json"
# Usage: python -m 蓝图格式.原序号字典.创世之书.创世字典构建
# 读取JSON文件
with open(json路径, 'r', encoding='utf-8') as f:
    data = json.load(f)

序号转模型 = {}
模型转序号 = {}
序号转图标 = {}
图标转序号 = {}

for item in data:
    item_id = item.get("ID", 0)
    item_name = item.get("Name", "")
    grid_index = item.get("GridIndex", 0)
    model_index = item.get("ModelIndex", 0)

    if model_index > 0 and item_name:
        序号转模型[model_index] = item_name
        模型转序号[item_name] = model_index
    if item_id > 0 and item_name:
        序号转图标[item_id] = item_name
        图标转序号[item_name] = item_id

# 模型
模型字符串 = 文件头部注释与导入()
模型字符串 += "\n创世_序号转模型: Dict[int, str]  = {\n"
for key in sorted(序号转模型.keys()):
    模型字符串 += f'    {key}: "{序号转模型[key]}",\n'
模型字符串 += "}\n"
模型字符串 += "\n创世_模型转序号: Dict[int, str]  = {\n"
for key in sorted(模型转序号.keys()):
    模型字符串 += f'    "{key}": {模型转序号[key]},\n'
模型字符串 += "}\n"

路径_创世_序号转模型 = Path(蓝图格式目录()) / "序号字典" / "创世之书31_模型与序号.py"
with open(路径_创世_序号转模型, "w", encoding="utf-8") as f:
    f.write(模型字符串)

# 图标
建筑字符串 = 文件头部注释与导入()
建筑字符串 += "\n创世_序号转图标: Dict[int, str]  = {\n"
for key in sorted(序号转图标.keys()):
    建筑字符串 += f'    {key}: "{序号转图标[key]}",\n'
建筑字符串 += "}\n"
建筑字符串 += "\n创世_图标转序号: Dict[int, str]  = {\n"
for key in sorted(图标转序号.keys()):
    建筑字符串 += f'    "{key}": {图标转序号[key]},\n'
建筑字符串 += "}\n"

路径_创世_图标与序号 = Path(蓝图格式目录()) / "序号字典" / "创世之书31_图标与序号.py"
with open(路径_创世_图标与序号, "w", encoding="utf-8") as f:
    f.write(建筑字符串)
