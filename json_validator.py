import json
import re

def find_illegal_commas(json_string):
    """
    查找JSON字符串中的非法逗号位置
    """
    illegal_comma_positions = []
    
    # 查找尾随逗号 (trailing commas)
    # 匹配 }, 或 ],
    trailing_comma_pattern = r'[,][\s\n\r]*[}\]]'
    for match in re.finditer(trailing_comma_pattern, json_string):
        comma_pos = match.start()
        illegal_comma_positions.append({
            'position': comma_pos,
            'type': 'trailing_comma',
            'context': json_string[max(0, comma_pos-10):comma_pos+15]
        })
    
    # 查找缺少值的逗号
    # 匹配逗号后直接跟闭合括号的情况
    missing_value_pattern = r'[,][\s\n\r]*[,}]'
    for match in re.finditer(missing_value_pattern, json_string):
        comma_pos = match.start()
        # 确认这不是尾随逗号的情况
        if json_string[match.end()-1] != ']':
            illegal_comma_positions.append({
                'position': comma_pos,
                'type': 'missing_value',
                'context': json_string[max(0, comma_pos-10):comma_pos+15]
            })
            
    return illegal_comma_positions

def fix_json_commas(json_string):
    """
    自动修复JSON中的非法逗号
    """
    # 移除对象和数组末尾的逗号
    fixed_json = re.sub(r',([\s\n\r]*[}\]])', r'\1', json_string)
    
    return fixed_json

def validate_and_fix_json(file_path):
    """
    验证并尝试修复JSON文件
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 尝试解析原始JSON
        try:
            json.loads(content)
            print(f"✓ {file_path} 是有效的JSON文件")
            return True
        except json.JSONDecodeError as e:
            print(f"✗ {file_path} 包含无效JSON:")
            print(f"  错误信息: {e}")
            
            # 查找非法逗号
            illegal_commas = find_illegal_commas(content)
            if illegal_commas:
                print(f"  发现 {len(illegal_commas)} 处非法逗号:")
                for i, comma_info in enumerate(illegal_commas):
                    print(f"    {i+1}. 位置 {comma_info['position']} - {comma_info['type']}")
                    print(f"       上下文: ...{comma_info['context'].strip()}...")
                
                # 尝试自动修复
                fixed_content = fix_json_commas(content)
                try:
                    json.loads(fixed_content)
                    print("  自动修复成功!")
                    
                    # 保存修复后的文件
                    backup_path = file_path + '.backup'
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    
                    print(f"  已保存修复后的文件到: {file_path}")
                    print(f"  原始文件已备份到: {backup_path}")
                    
                    # 将原文件重命名为备份
                    import shutil
                    shutil.copy(file_path.replace('.backup', ''), backup_path)
                    
                    return True
                except json.JSONDecodeError:
                    print("  自动修复失败，请手动检查文件")
                    return False
            else:
                print("  未发现明显的逗号问题，请手动检查其他语法错误")
                return False
                
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
        return False
    except Exception as e:
        print(f"处理文件时出错: {e}")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        validate_and_fix_json(file_path)
    else:
        print("用法: python json_validator.py <json_file_path>")
        print("示例: python json_validator.py data.json")