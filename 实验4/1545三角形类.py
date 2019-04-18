#!/anaconda3/bin/python
# @Time    : 2019-04-03 08:24
# @Author  : zhou
# @File    : 1545三角形类
# @Software: PyCharm
# @Description: 

import math


class GeometricObject:
    """几何对象"""

    def __init__(self, color, filled):
        self.__color = color
        self.__filled = filled


class Triangle(GeometricObject):
    """三角形类"""

    def __init__(self, color, filled, slide1=1.0, slide2=1.0, slide3=1.0):
        super().__init__(color, filled)
        self.__slide1 = slide1
        self.__slide2 = slide2
        self.__slide3 = slide3
        print("Triangle: side1=%.1f side2=%.1f side3=%.1f color=%s filled=%s" % (slide1, slide2, slide3, color, filled))

    def getArea(self):
        """:return 三角形面积"""
        p = self.getPerimeter() / 2
        return math.sqrt(p * (p - self.__slide1) * (p - self.__slide2) * (p - self.__slide3))

    def getPerimeter(self):
        """:return 三角形周长"""
        return self.__slide1 + self.__slide2 + self.__slide3


slide1, slide2, slide3, color, filled = input().split()
a = Triangle(color, filled, float(slide1), float(slide2), float(slide3))
print('Area=' + str('%.2f' % a.getArea()))
print('Perimeter=' + str('%.2f' % a.getPerimeter()))
