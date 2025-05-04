import base64
import gzip

from 蓝图格式 import 类型
from 蓝图格式.中段 import 蓝图中段
from 蓝图格式.中段杂项 import 中段杂项
from 蓝图格式.区域 import 区域
from 蓝图格式.图标 import 图标 as 图标类
from 蓝图格式.坐标 import Int32平面坐标, Int16平面坐标, 普通建筑姿态, 传送带姿态, 全空间姿态, 分拣器姿态
from 蓝图格式.建筑 import 建筑, 建筑主导接口
from 蓝图格式.模型 import 模型 as 模型类
from 蓝图格式.额外参数 import 额外参数之未解析


# Base64 编码的字符串示意
# r"H4sIAAAAAAAAC2NkQAWMUAxh/2dgOAFlMoKFZ////x/Ev8iujKRngqQ5A4OJM4j9HwqQjGEAADRnUB9kAAAA"

class 比特流解析器:
    def __init__(self, 十六进制数):
        self.offset = 0
        self.十六进制数 = 十六进制数

    def 解析(self, 格式) -> tuple:
        import struct
        result = struct.unpack_from(格式, self.十六进制数, self.offset)
        self.offset += struct.calcsize(格式)
        return result

    def 解析杂项(self) -> 中段杂项:
        (
            version,
            cursorOffset_x,
            cursorOffset_y,
            cursorTargetArea,
            dragBoxSize_x,
            dragBoxSize_y,
            primaryAreaIdx,
        ) = self.解析("<7i")
        l_光标锚点偏移坐标 = Int32平面坐标(
            东西X=类型.Int32(cursorOffset_x),
            南北Y=类型.Int32(cursorOffset_y)
        )
        l_拖拽框大小 = Int32平面坐标(
            东西X=类型.Int32(dragBoxSize_x),
            南北Y=类型.Int32(dragBoxSize_y)
        )
        return 中段杂项(
            版本=类型.Int32(version),
            光标锚点偏移坐标=l_光标锚点偏移坐标,
            光标对应区域=类型.Int32(cursorTargetArea),
            拖拽框大小=l_拖拽框大小,
            主区域索引=类型.Int32(primaryAreaIdx)
        )

    def 解析区域(self) -> list[区域]:
        (区域数,) = self.解析("b")
        所有区域 = []
        for i in range(区域数):
            (
                index,
                parent_index,
                tropicAnchor,
                areaSegments,
                anchorLocalOffset_x,
                anchorLocalOffset_y,
                Size_x,
                Size_y,
            ) = self.解析("<bbhhhhhh")
            锚点偏移 = Int16平面坐标(
                东西X=类型.Int16(anchorLocalOffset_x),
                南北Y=类型.Int16(anchorLocalOffset_y)
            )
            大小 = Int16平面坐标(
                东西X=类型.Int16(Size_x),
                南北Y=类型.Int16(Size_y)
            )
            当前区域 = 区域(
                区域序号=类型.Int8(index),
                父区域序号=类型.Int8(parent_index),
                tropic_anchor=类型.Int16(tropicAnchor),
                area_segments=类型.Int16(areaSegments),
                锚点偏移=锚点偏移,
                大小=大小,
            )
            所有区域.append(当前区域)
        return 所有区域

    def 解析普通建筑姿态(self) -> 普通建筑姿态:
        (
            localOffset_x,
            localOffset_y,
            localOffset_z,
            yaw
        ) = self.解析("<4f")
        return 普通建筑姿态(
            东西X=localOffset_x,
            南北Y=localOffset_y,
            高度Z=localOffset_z,
            水平旋转Z=yaw,
        )

    def 解析传送带姿态(self) -> 传送带姿态:
        (
            localOffset_x,
            localOffset_y,
            localOffset_z,
            yaw,
            roll
        ) = self.解析("<5f")
        return 传送带姿态(
            东西X=localOffset_x,
            南北Y=localOffset_y,
            高度Z=localOffset_z,
            水平旋转Z=yaw,
            左右倾斜X=roll,
        )

    def 解析全空间姿态(self) -> 全空间姿态:
        (
            localOffset_x,
            localOffset_y,
            localOffset_z,
            yaw,
            roll,
            pitch
        ) = self.解析("<6f")
        return 全空间姿态(
            东西X=localOffset_x,
            南北Y=localOffset_y,
            高度Z=localOffset_z,
            水平旋转Z=yaw,
            左右倾斜X=roll,
            上下翻滚Y=pitch,
        )

    def 解析分拣器姿态(self) -> 分拣器姿态:
        return 分拣器姿态(
            起点=self.解析全空间姿态(),
            终点=self.解析全空间姿态(),
        )

    def 解析建筑(self) -> list[建筑]:
        (建筑数,) = self.解析("i")
        所有建筑 = []
        for i in range(建筑数):
            num, = self.解析("i")
            assert num == -101
            (
                index,
                itemId,
                modelIndex,
                areaIndex,
            ) = self.解析("<iHHb")

            if 2000 < itemId < 2010:
                姿态 = self.解析传送带姿态()
            elif 2010 <= itemId < 2020:
                姿态 = self.解析分拣器姿态()
            else:
                姿态 = self.解析普通建筑姿态()

            (
                outputObjIdx,
                inputObjIdx,
                outputToSlot,
                inputFromSlot,
                outputFromSlot,
                inputToSlot,
                outputOffset,
                inputOffset,
                recipeId,
                filterId,
                parameterLength,
            ) = self.解析("iiBBBBBBHHH")

            parameter = self.解析("i" * parameterLength)
            l_额外参数 = 额外参数之未解析(
                参数=[类型.Int32(x) for x in parameter]
            )
            l_额外参数 = l_额外参数.尝试解析(modelIndex)

            输出接口 = 建筑主导接口(
                目标序号=类型.Int32(outputObjIdx),
                目标接口=类型.Int8(outputToSlot),
                自身接口=类型.Int8(outputFromSlot),
                插槽偏移=类型.Int8(outputOffset)
            )
            输入接口 = 建筑主导接口(
                目标序号=类型.Int32(inputObjIdx),
                目标接口=类型.Int8(inputToSlot),
                自身接口=类型.Int8(inputFromSlot),
                插槽偏移=类型.Int8(inputOffset)
            )

            当前建筑 = 建筑(
                建筑序号=类型.Int32(index),
                区域序号=类型.Int8(areaIndex),
                物品序号=图标类(itemId),
                模型序号=模型类(modelIndex),
                空间姿态=姿态,
                输出接口=输出接口,
                输入接口=输入接口,
                配方序号=类型.UInt16(recipeId),
                过滤物品序号=图标类(filterId),
                额外参数=l_额外参数
            )
            所有建筑.append(当前建筑)
        return 所有建筑


def Base64解析(Base64字符) -> str:
    解码 = base64.b64decode(Base64字符)
    解压缩 = gzip.decompress(解码)
    # 十六进制数 = 解压缩.hex()
    return 解压缩


def 解析中段(中段字符) -> 蓝图中段:
    十六进制数 = Base64解析(中段字符)
    流解析器 = 比特流解析器(十六进制数)
    l_杂项 = 流解析器.解析杂项()
    l_区域 = 流解析器.解析区域()
    l_建筑 = 流解析器.解析建筑()
    return 蓝图中段(
        杂项=l_杂项,
        区域=l_区域,
        建筑=l_建筑
    )


if __name__ == '__main__':
    字符串 = r"""
    H4sIAAAAAAAAC2NkQAWMUAxh/2dgOAFlMoKFZ////x/Ev8iujKRngqQ5A4OJM4j9HwqQjGEAADRnUB9kAAAA
    """
    中段 = 解析中段(字符串.strip())
    print(中段)
