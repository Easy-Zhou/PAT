#!/anaconda3/bin/python
# @Time    : 2019-04-04 12:26
# @Author  : zhou
# @File    : 1553圆柱类的实现
# @Software: PyCharm
# @Description: 

PI = 3.14


class Cylinder:
    """圆柱体类"""

    def __init__(self, radius, height):
        self.__radius = radius
        self.__height = height

    def getVolume(self):
        """计算圆柱体的体积"""
        return round(PI * self.__radius ** 2 * self.__height, 2)


radius, height = map(int, input().split())
cylinder = Cylinder(radius, height)
print("%.2f" % cylinder.getVolume())
