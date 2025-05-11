_调试开启 = True

def 正在加载(文件名):
    日志("正在加载: " + 文件名)

def 加载完成(文件名):
    日志("加载完成: " + 文件名)

def 警告(警告信息):
    日志("警告: " + 警告信息)

def 调试(警告信息):
    if _调试开启:
        日志("调试: " + 警告信息)

def 信息(警告信息):
    日志("信息: " + 警告信息)

def 未完成的函数(str):
    raise Exception("函数还没写完")

def 纯虚函数():
    raise Exception(f"尝试执行纯虚函数")

def 确保类型(输入, 类型: type):
    if isinstance(输入, type):
        raise Exception(f"输入类型错误:{输入.__class__}")

def 日志(str):
    print(str)

