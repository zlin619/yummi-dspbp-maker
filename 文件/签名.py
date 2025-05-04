# 如果你看到这个文件, 想必你已经看过仙祖的md5校验文件了
# 作为全工程少数几个纯英文文件,我建议别动
# 我是一点都看不懂,甚至怕改着改着挂了
# 你看我甚至给他包了一层,我是一个字符都不想动

from 文件.DysonSphereMD5 import DysonSphereMD5

def 签名(未签名蓝图) -> str:
    if isinstance(未签名蓝图, str):
        未签名蓝图 = 未签名蓝图.encode('utf-8')
    elif isinstance(未签名蓝图, bytes):
        pass
    else:
        raise TypeError('未签名蓝图必须为字符串str或bytearray')

    return(DysonSphereMD5(variant = DysonSphereMD5.Variant.MD5F).update(未签名蓝图).hexdigest().upper())

def 签名的蓝图(未签名蓝图: str) -> str:
    return 未签名蓝图 + '"' + 签名(未签名蓝图)
