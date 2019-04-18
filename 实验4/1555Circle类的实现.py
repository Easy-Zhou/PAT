#!/anaconda3/bin/python
# @Time    : 2019-04-04 12:30
# @Author  : zhou
# @File    : 1555Circle类的实现
# @Software: PyCharm
# @Description: 

PI = 3.14


class Circle:
    """Circle类"""

    def __init__(self, x=0, y=0, radius=1):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def calDiameter(self):
        """计算直径"""
        return self.__radius * 2

    def calArea(self):
        """计算面积"""
        return round(PI * self.__radius ** 2, 1)

    def calPerimeter(self):
        """计算周长"""
        return round(2 * PI * self.__radius, 1)

    def output(self):
        """输出"""
        print('Center(%d,%d) and Radius=%d' % (self.__x, self.__y, self.__radius))
        print('Diameter=%d' % self.calDiameter())
        print('Area=%.1f' % self.calArea())
        print('Perimeter=%.1f' % self.calPerimeter())


input_in = list(map(int, input().split()))
circle = Circle(*input_in)
circle.output()
