import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sys
import os

# 添加路径处理函数，解决打包后资源文件找不到的问题
def resource_path(relative_path):
    """获取资源文件的绝对路径"""
    try:
        # PyInstaller创建临时文件夹，将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)



# 恢复原始导入方式
from 文件.文件读写 import 读取txt文件, 读取json文件
from 蓝图格式.坐标 import 空间坐标
from 蓝图格式.蓝图 import 蓝图

class 蓝图工具UI:
    # 使用 grid 布局实现左中右各占 1/3
    def __init__(self, root):
        self.root = root
        self.root.title("悠米蓝图工具")
        self.root.geometry("1400x800")  # 设置窗口大小
        
        # 设置窗口图标
        try:
            # 使用resource_path函数获取图标路径
            icon_path = resource_path("门扉秘典.ico")
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)  # 使用.ico格式的图标文件
            else:
                print(f"图标文件不存在: {icon_path}")
        except tk.TclError:
            print("图标加载失败，使用默认图标")
            pass
        except Exception as e:
            print(f"图标加载异常: {e}")


    def _从文本读取(self) -> 蓝图:
        输入文本 = self.text_entry.get(1.0, tk.END).strip()
        if not 输入文本:
            messagebox.showerror("错误", "请输入文本内容")
            return
        # 使用读取泛蓝图文本处理
        from 文件.文件读写 import 读取泛蓝图文本
        try:
            return 读取泛蓝图文本(输入文本)
        except Exception as e:
            messagebox.showerror("文本转换失败", str(e))

    def _从文件读取(self) -> 蓝图:
        # 从文件路径获取内容
        文件路径 = self.file_entry.get().strip()
        if not 文件路径:
            messagebox.showerror("错误", "请输入文件路径")
            return
        # 使用读取泛蓝图文件处理
        from 文件.文件读写 import 读取泛蓝图文件
        try:
            return 读取泛蓝图文件(文件路径)
        except Exception as e:
            messagebox.showerror("文件转换失败", str(e))


    def _执行平移转换(self):
        本蓝图 = self._读取蓝图()
        x_value = self.平移X文本框.get()
        y_value = self.平移Y文本框.get()
        z_value = self.平移Z文本框.get()
        try:
            x = float(x_value) if x_value else 0.0
            y = float(y_value) if y_value else 0.0
            z = float(z_value) if z_value else 0.0
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            return
        # 修改导入方式和调用方式
        from 功能.平移缩放 import 平移缩放
        平移缩放(本蓝图).建筑平移(空间坐标(x, y ,z))
        self._显示蓝图输出(本蓝图)

    def _执行缩放转换(self):
        本蓝图 = self._读取蓝图()
        x_value = self.缩放X文本框.get()  # 使用缩放专用输入框
        y_value = self.缩放Y文本框.get()  # 使用缩放专用输入框
        z_value = self.缩放Z文本框.get()  # 使用缩放专用输入框
        try:
            x = float(x_value) if x_value else 1.0
            y = float(y_value) if y_value else 1.0
            z = float(z_value) if z_value else 1.0
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            return
        # 修改导入方式和调用方式
        from 功能.平移缩放 import 平移缩放
        平移缩放(本蓝图).建筑缩放(空间坐标(x, y, z))
        self._显示蓝图输出(本蓝图)

    def _执行删锚点转换(self):
        from 功能.单格锚点 import 转换为单锚点
        本蓝图 = self._读取蓝图()
        转换为单锚点(本蓝图)
        self._显示蓝图输出(本蓝图)


