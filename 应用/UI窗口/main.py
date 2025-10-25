import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys

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
            # 如果是直接运行Python脚本
            application_path = os.path.dirname(os.path.abspath(__file__))
            icon_path = os.path.join(application_path, "门扉秘典.ico")
            
            # 确保图标文件存在再设置
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
                print(f"成功加载图标: {icon_path}")
            else:
                print(f"图标文件不存在: {icon_path}")
        except tk.TclError as e:
            print(f"图标加载失败，使用默认图标: {e}")
        except Exception as e:
            print(f"图标加载出错: {e}")

        # 配置 grid 布局，确保窗口分为 3 列 2 行
        for i in range(3):  # 配置 3 列
            self.root.columnconfigure(i, weight=1, uniform="column")
        self.root.rowconfigure(0, weight=0, minsize=50)
        self.root.rowconfigure(1, weight=1)  # 第二行高度自适应

        # 左上区域：输入区域
        self.输入标题区域 = tk.Frame(self.root, bg="lightyellow")
        self.输入标题区域.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # 中上区域：转换模式区域
        self.转换标题区域 = tk.Frame(self.root, bg="lightyellow")
        self.转换标题区域.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # 右上区域：输出区域
        self.输出标题区域 = tk.Frame(self.root, bg="lightyellow")
        self.输出标题区域.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        # 左下区域：额外功能（可扩展）
        self.输入工作区域 = tk.Frame(self.root, bg="lightyellow")
        self.输入工作区域.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # 中下区域：额外功能（可扩展）
        self.转换工作区域 = tk.Frame(self.root, bg="lightyellow")
        self.转换工作区域.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        # 右下区域：额外功能（可扩展）
        self.输出工作区域 = tk.Frame(self.root, bg="lightyellow")
        self.输出工作区域.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        # 初始化输入、输出和转换模式
        self._初始化输入标题区域()
        self._初始化转换标题区域()
        self._初始化输出标题区域()
        self._初始化输入工作区域()
        self._初始化转换工作区域()
        self._初始化输出工作区域()
        

    def _初始化输入标题区域(self):
        # 示例：在中间转换模式区域添加控件
        label = tk.Label(self.输入标题区域, text="输入区域", font=("Arial", 14), bg="lightyellow")
        label.pack(pady=10)

    def _初始化转换标题区域(self):
        # 示例：在中间转换模式区域添加控件
        label = tk.Label(self.转换标题区域, text="转换模式", font=("Arial", 14), bg="lightyellow")
        label.pack(pady=10)

    def _初始化输出标题区域(self):
        # 示例：在右侧输出区域添加控件
        label = tk.Label(self.输出标题区域, text="输出区域", font=("Arial", 14), bg="lightyellow")
        label.pack(pady=10)

    def _初始化输入工作区域(self):
        # 创建选项卡
        self.输入选项卡 = ttk.Notebook(self.输入工作区域)
        self.输入选项卡.pack(fill=tk.BOTH, expand=True)

        # 第一个选项卡：从文本读取（交换后放在前面）
        self.text_tab = tk.Frame(self.输入选项卡, bg="lightyellow")
        self.输入选项卡.add(self.text_tab, text="从文本读取")
        self._初始化文本读取选项卡()

        # 第二个选项卡：从文件读取（交换后放在后面）
        self.file_tab = tk.Frame(self.输入选项卡, bg="lightyellow")
        self.输入选项卡.add(self.file_tab, text="从文件读取")
        self._初始化文件读取选项卡()

    def _初始化文件读取选项卡(self):
        # 使用grid布局使文件输入部分与输出区域对齐
        file_label = tk.Label(self.file_tab, text="文件名：", font=("Arial", 12), bg="lightyellow")
        file_label.grid(row=0, column=0, padx=20, pady=5, sticky="n")
        self.file_entry = tk.Entry(self.file_tab, width=40)
        self.file_entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="n")
        
        # 添加按钮区域
        file_button_frame = tk.Frame(self.file_tab, bg="lightyellow")
        file_button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        # 添加浏览文件按钮
        browse_button = tk.Button(file_button_frame, text="浏览文件", command=self._浏览文件)
        browse_button.pack(side=tk.LEFT, padx=5)
        
        # 添加加载文件按钮
        load_button = tk.Button(file_button_frame, text="预览文件", command=self._预览文件)
        load_button.pack(side=tk.LEFT, padx=5)

        # 配置列权重
        self.file_tab.columnconfigure(0, weight=1)
        self.file_tab.columnconfigure(1, weight=1)

    def _初始化文本读取选项卡(self):
        # 文本输入框 - 采用类似输出区域的布局
        text_label = tk.Label(self.text_tab, text="输入文本：", font=("Arial", 12), bg="lightyellow")
        text_label.grid(row=0, column=0, padx=20, pady=5, sticky="n")
        
        # 按钮区域 - 放在右上角
        text_button_frame = tk.Frame(self.text_tab, bg="lightyellow")
        text_button_frame.grid(row=0, column=1, padx=20, pady=5, sticky="n")  # 居中显示，左右留白
        
        # 从剪贴板粘贴按钮
        clipboard_button = tk.Button(text_button_frame, text="从剪贴板粘贴", command=self._从剪贴板粘贴)
        clipboard_button.pack(side=tk.LEFT, padx=5)

        # 大文本输入框 - 放在下方
        self.text_entry = tk.Text(self.text_tab, height=10, width=40)
        self.text_entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="n")
 
        # 配置行权重，使文本框可以随窗口大小调整
        self.text_tab.rowconfigure(1, weight=1)
        
        # 配置列权重
        self.text_tab.columnconfigure(0, weight=1)
        self.text_tab.columnconfigure(1, weight=1)

    def _从剪贴板粘贴(self):
        try:
            clipboard_content = self.root.clipboard_get()
            self.text_entry.delete(1.0, tk.END)
            self.text_entry.insert(tk.END, clipboard_content)
        except tk.TclError:
            messagebox.showerror("错误", "无法获取剪贴板内容")

    def _初始化转换工作区域(self):
        # 创建选项卡控件
        self.转换_notebook = ttk.Notebook(self.转换工作区域)
        self.转换_notebook.pack(fill=tk.BOTH, expand=True)

        # 基础选项卡
        self.基础_tab = tk.Frame(self.转换_notebook, bg="lightyellow")
        self.转换_notebook.add(self.基础_tab, text="基础")
        self._初始化基础选项卡()

        # 平移选项卡
        self.平移_tab = tk.Frame(self.转换_notebook, bg="lightyellow")
        self.转换_notebook.add(self.平移_tab, text="平移")
        self._初始化平移选项卡()

        # 缩放选项卡
        self.缩放_tab = tk.Frame(self.转换_notebook, bg="lightyellow")
        self.转换_notebook.add(self.缩放_tab, text="缩放")
        self._初始化缩放选项卡()

        # 删锚点选项卡
        self.删锚点_tab = tk.Frame(self.转换_notebook, bg="lightyellow")
        self.转换_notebook.add(self.删锚点_tab, text="删锚点")
        self._初始化删锚点选项卡()

        # 浮空仙术选项卡
        self.浮空仙术_tab = tk.Frame(self.转换_notebook, bg="lightyellow")
        self.转换_notebook.add(self.浮空仙术_tab, text="浮空仙术")
        self._初始化浮空仙术选项卡()

    def _初始化基础选项卡(self):
        # 添加转换按钮
        convert_button = tk.Button(self.基础_tab, text="转换", command=self._执行基础转换)
        convert_button.pack(pady=10)

    def _初始化平移选项卡(self):
        # X轴平移设置
        x_frame = tk.Frame(self.平移_tab, bg="lightyellow")
        x_frame.pack(pady=5)
        x_label = tk.Label(x_frame, text="X轴:", bg="lightyellow")
        x_label.pack(side=tk.LEFT)
        self.平移X文本框 = tk.Entry(x_frame, width=10)  # 专门为平移选项卡创建的输入框
        self.平移X文本框.pack(side=tk.LEFT, padx=5)
        
        # Y轴平移设置
        y_frame = tk.Frame(self.平移_tab, bg="lightyellow")
        y_frame.pack(pady=5)
        y_label = tk.Label(y_frame, text="Y轴:", bg="lightyellow")
        y_label.pack(side=tk.LEFT)
        self.平移Y文本框 = tk.Entry(y_frame, width=10)  # 专门为平移选项卡创建的输入框
        self.平移Y文本框.pack(side=tk.LEFT, padx=5)
        
        # Z轴平移设置
        z_frame = tk.Frame(self.平移_tab, bg="lightyellow")
        z_frame.pack(pady=5)
        z_label = tk.Label(z_frame, text="Z轴:", bg="lightyellow")
        z_label.pack(side=tk.LEFT)
        self.平移Z文本框 = tk.Entry(z_frame, width=10)  # 专门为平移选项卡创建的输入框
        self.平移Z文本框.pack(side=tk.LEFT, padx=5)
        
        # 添加转换按钮
        convert_button = tk.Button(self.平移_tab, text="转换", command=self._执行平移转换)
        convert_button.pack(pady=10)

    def _初始化缩放选项卡(self):
        # X轴缩放设置
        x_frame = tk.Frame(self.缩放_tab, bg="lightyellow")
        x_frame.pack(pady=5)
        x_label = tk.Label(x_frame, text="X轴:", bg="lightyellow")
        x_label.pack(side=tk.LEFT)
        self.缩放X文本框 = tk.Entry(x_frame, width=10)  # 专门为缩放选项卡创建的输入框
        self.缩放X文本框.pack(side=tk.LEFT, padx=5)
        
        # Y轴缩放设置
        y_frame = tk.Frame(self.缩放_tab, bg="lightyellow")
        y_frame.pack(pady=5)
        y_label = tk.Label(y_frame, text="Y轴:", bg="lightyellow")
        y_label.pack(side=tk.LEFT)
        self.缩放Y文本框 = tk.Entry(y_frame, width=10)  # 专门为缩放选项卡创建的输入框
        self.缩放Y文本框.pack(side=tk.LEFT, padx=5)

        # Z轴缩放设置
        z_frame = tk.Frame(self.缩放_tab, bg="lightyellow")
        z_frame.pack(pady=5)
        z_label = tk.Label(z_frame, text="Z轴:", bg="lightyellow")
        z_label.pack(side=tk.LEFT)
        self.缩放Z文本框 = tk.Entry(z_frame, width=10)  # 专门为缩放选项卡创建的输入框
        self.缩放Z文本框.pack(side=tk.LEFT, padx=5)

        # 添加转换按钮
        convert_button = tk.Button(self.缩放_tab, text="转换", command=self._执行缩放转换)
        convert_button.pack(pady=10)

    def _初始化删锚点选项卡(self):
        convert_button = tk.Button(self.删锚点_tab, text="转换", command=self._执行删锚点转换)
        convert_button.pack(pady=10)
        
    def _初始化浮空仙术选项卡(self):
        convert_button = tk.Button(self.浮空仙术_tab, text="转换", command=self._执行浮空仙术转换)
        convert_button.pack(pady=10)

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
    # 新增的转换方法
    def _读取蓝图(self) -> 蓝图:
        # 基础转换逻辑
        # 检查当前选中的输入选项卡
        输入选项卡ID = self.输入选项卡.select()
        当前输入标签页 = self.输入选项卡.tab(输入选项卡ID, "text")
        self._清理文本框残留数据()

        if 当前输入标签页 == "从文本读取":
            本蓝图 = self._从文本读取()
            
        elif 当前输入标签页 == "从文件读取":
            本蓝图 = self._从文件读取()
        else:
            messagebox.showerror("错误", "未知的输入方式")
        from 功能.指鹿为马.通用 import 强制纠正姿态
        from 应用.版本修正 import 版本修正
        强制纠正姿态(本蓝图)
        版本修正(本蓝图)
        return 本蓝图

    def _执行基础转换(self):
        本蓝图 = self._读取蓝图()
        self._显示蓝图输出(本蓝图)

    def _执行平移转换(self):
        本蓝图 = self._读取蓝图()
        x_value = self.平移X文本框.get()  # 使用平移专用输入框
        y_value = self.平移Y文本框.get()  # 使用平移专用输入框
        z_value = self.平移Z文本框.get()  # 使用平移专用输入框
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

    def _执行浮空仙术转换(self):
        本蓝图 = self._读取蓝图()
        from 功能.浮空地基 import 添加仙术地基
        添加仙术地基(本蓝图)
        self._显示蓝图输出(本蓝图)

    def _显示蓝图输出(self, 蓝图对象: 蓝图):
        self._清理文本框残留数据()
        if not 蓝图对象: return
        try:
            json_str = 蓝图对象.转json()
            import json
            self.json文本框.insert(tk.END, json.dumps(json_str, ensure_ascii=False, indent=4))
        except Exception as e:
            messagebox.showerror("Json输出错误", str(e))
            pass
        try:
            blueprint_str = 蓝图对象.转蓝图字符串()
            self.二进制蓝图文本框.insert(tk.END, blueprint_str)
        except Exception as e:
            messagebox.showerror("二进制蓝图输出错误", str(e))

    def _清理文本框残留数据(self):
        self.json文本框.delete(1.0, tk.END)
        self.二进制蓝图文本框.delete(1.0, tk.END)

    def _初始化输出工作区域(self):
        # 蓝图 JSON 输出区域
        json_label = tk.Label(self.输出工作区域, text="蓝图 JSON", font=("Arial", 12), bg="lightyellow")
        json_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")  # 改为west对齐
        json_button_frame = tk.Frame(self.输出工作区域, bg="lightyellow")
        json_button_frame.grid(row=0, column=1, pady=5, sticky="w")  # 靠左对齐，右边保留一点间距
        json_copy_input_button = tk.Button(json_button_frame, text="复制到输入", command=lambda: self._复制到输入(self.json文本框))
        json_copy_input_button.pack(side=tk.LEFT, padx=5)
        json_copy_clipboard_button = tk.Button(json_button_frame, text="复制到剪贴板", command=lambda: self._复制到剪贴板(self.json文本框))
        json_copy_clipboard_button.pack(side=tk.LEFT, padx=5)
        self.json文本框 = tk.Text(self.输出工作区域, height=10, width=40)
        self.json文本框.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="n")  # 居中显示，左右留白

        # 二进制蓝图输出区域
        binary_label = tk.Label(self.输出工作区域, text="二进制蓝图", font=("Arial", 12), bg="lightyellow")
        binary_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")  # 改为west对齐
        binary_button_frame = tk.Frame(self.输出工作区域, bg="lightyellow")
        binary_button_frame.grid(row=2, column=1, pady=5, sticky="w")  # 靠左对齐，右边保留一点间距
        binary_copy_input_button = tk.Button(binary_button_frame, text="复制到输入", command=lambda: self._复制到输入(self.二进制蓝图文本框))
        binary_copy_input_button.pack(side=tk.LEFT, padx=5)
        binary_copy_clipboard_button = tk.Button(binary_button_frame, text="复制到剪贴板", command=lambda: self._复制到剪贴板(self.二进制蓝图文本框))
        binary_copy_clipboard_button.pack(side=tk.LEFT, padx=5)
        self.二进制蓝图文本框 = tk.Text(self.输出工作区域, height=10, width=40)
        self.二进制蓝图文本框.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="n")  # 居中显示，左右留白

        # 输出到文件区域
        file_label = tk.Label(self.输出工作区域, text="输出到文件（这功能没做）", font=("Arial", 12), bg="lightyellow")
        file_label.grid(row=4, column=0, padx=20, pady=5, sticky="w")  # 改为west对齐
        file_button_frame = tk.Frame(self.输出工作区域, bg="lightyellow")
        file_button_frame.grid(row=4, column=1, padx=(0,20), pady=5, sticky="w")  # 靠左对齐，右边保留一点间距
        self.file_output = tk.Text(self.输出工作区域, height=10, width=40)
        self.file_output.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="n")  # 居中显示，左右留白

        # 配置列权重，确保布局自适应
        self.输出工作区域.columnconfigure(0, weight=1)
        self.输出工作区域.columnconfigure(1, weight=1)

    def _复制到输入(self, source_text_widget):  
        # 获取源文本框的内容
        content = source_text_widget.get(1.0, tk.END).strip()
        self.text_entry.delete(1.0, tk.END)
        self.text_entry.insert(tk.END, content)
        # 切换选项卡到文本框那一页
        self.输入选项卡.select(self.text_tab)

    def _复制到剪贴板(self, source_text_widget):
        # 获取源文本框的内容并复制到剪贴板
        content = source_text_widget.get(1.0, tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(content)

    def _浏览文件(self):
        file_path = filedialog.askopenfilename(
            title="选择文件",
            filetypes=[("Text files", "*.txt"), ("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def _预览文件(self):
        # 获取文件路径
        file_path = self.file_entry.get().strip()
        if not file_path:
            messagebox.showerror("错误", "请输入文件路径或浏览选择文件")
            return
        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            # 清空文本输入框并插入文件内容
            self.text_entry.delete(1.0, tk.END)
            self.text_entry.insert(tk.END, content)
            # 切换到文本输入选项卡
            self.输入选项卡.select(self.text_tab)
        except FileNotFoundError:
            messagebox.showerror("错误", "文件未找到")
        except Exception as e:
            messagebox.showerror("错误", f"读取文件时发生错误: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = 蓝图工具UI(root)
    root.mainloop()
