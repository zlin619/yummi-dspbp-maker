import os
import subprocess
import sys
#python -m 应用.UI窗口.打包

def build_project():
    # 定义路径
    # 修改: 正确计算项目根目录为当前文件的上两级目录
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ui_window_dir = os.path.join(project_root, "应用", "UI窗口")
    main_py = os.path.join(ui_window_dir, "main.py")
    icon_path = os.path.join(ui_window_dir, "门扉秘典.ico")
    dist_path = os.path.join(project_root, 'dist')
    
    # 检查文件是否存在
    if not os.path.exists(main_py):
        print(f"错误: 找不到主程序文件 {main_py}")
        input("按回车键退出...")
        return False
        
    print(f"找到主程序文件: {main_py}")
    
    # 构建命令 - 使用完整的项目目录结构
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        f"--distpath={dist_path}",
        f"--workpath={os.path.join(project_root, 'build')}",
        f"--specpath={ui_window_dir}",
        # 添加所有项目路径以确保模块能被找到
        f"--paths={project_root}",
        f"--name=悠米蓝图工具",
        main_py
    ]
    
    # 如果图标存在，则添加图标参数
    if os.path.exists(icon_path):
        cmd.insert(4, f"--icon={icon_path}")
        print(f"使用图标文件: {icon_path}")
    else:
        print("警告: 未找到图标文件，将使用默认图标")
    
    print("\n执行命令:")
    print(" ".join(cmd))
    print()
    
    try:
        # 执行打包命令
        result = subprocess.run(cmd, check=True)
        print("\n打包成功完成！")
        
        # 检查图标是否成功打包
        exe_path = os.path.join(dist_path, "悠米蓝图工具.exe")
        if os.path.exists(exe_path) and os.path.exists(icon_path):
            print(f"可执行文件已生成: {exe_path}")
            print("图标应已正确应用到可执行文件")
        else:
            print("注意: 可执行文件已生成，但图标可能未正确应用")
            
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n打包失败: {e}")
        return False
    except FileNotFoundError:
        print("\n错误: 找不到 pyinstaller 命令")
        print("请先安装 PyInstaller:")
        print("pip install pyinstaller")
        return False

if __name__ == "__main__":
    build_project()