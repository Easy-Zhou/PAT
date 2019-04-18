#!/anaconda3/bin/python
# @Time    : 2019-04-03 08:13
# @Author  : zhou
# @File    : 1544长方体
# @Software: PyCharm
# @Description: 


class Cuboid:
    """长方体"""

    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def getBottomArea(self):
        """计算长方体底面积"""
        return self.__width * self.__length

    def getVolume(self):
        """计算长方体体积"""
        return self.__length * self.__width * self.__height


x, y, z = map(int, input().split())
cuboid = Cuboid(x, y, z)
print(cuboid.getBottomArea())
print(cuboid.getVolume())
