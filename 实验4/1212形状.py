#!/anaconda3/bin/python
# @Time    : 2019-04-03 00:44
# @Author  : zhou
# @File    : 1212形状
# @Software: PyCharm
# @Description: 

PI = 3.14


class Shape():
    """

    """

    def __init__(self):
        pass

    def superficial_area(self):
        """表面积"""
        pass

    def volume(self):
        """体积"""
        pass


class Cylinder(Shape):
    """圆柱体"""

    def __init__(self, radius=0.0, height=0.0):
        super().__init__()
        self.__radius = radius
        self.__height = height

    def superficial_area(self):
        """
        :return: 圆柱体表面积
        """
        return PI * self.__radius * self.__radius * 2 + 2 * PI * self.__radius * self.__height

    def volume(self):
        """
        :return: 圆柱体体积
        """
        return PI * self.__radius * self.__radius * self.__height


class Sphere(Shape):
    """球体"""

    def __init__(self, radius=0.0):
        super().__init__()
        self.__radius = radius

    def superficial_area(self):
        """
        :return: 球体表面积
        """
        return 4 * PI * self.__radius * self.__radius

    def volume(self):
        """
        :return: 球体体积
        """
        return PI * self.__radius ** 3 * 4 / 3


class Cube(Shape):
    """正方体"""

    def __init__(self, length=0.0):
        super().__init__()
        self.__length = length

    def superficial_area(self):
        """
        :return: 正方体表面积
        """
        return 6 * self.__length ** 2

    def volume(self):
        """
        :return: 正方体体积
        """
        return self.__length ** 3


class Cuboid(Shape):
    """正方体"""

    def __init__(self, length=0.0, width=0.0, height=0.0):
        super().__init__()
        self.__length = length
        self.__width = width
        self.__height = height

    def superficial_area(self):
        """
        :return: 正方体表面积
        """
        return 2 * (self.__length * (self.__height + self.__width) + self.__height * self.__width)

    def volume(self):
        """
        :return: 正方体体积
        """
        return self.__length * self.__width * self.__height

n = int(input())
for i in range(n):
    r,h = map(float, input().split())
    cylinder = Cylinder(r,h)

    r = float(input())
    sphere = Sphere(r)

    length = float(input())
    cube = Cube(length)

    x,y,z = map(float,input().split())
    cuboid = Cuboid(x, y, z)
    print("%.2f %.2f" % (round(cylinder.superficial_area(),2), round(cylinder.volume(),2)))
    print("%.2f %.2f" % (round(sphere.superficial_area(),2), round(sphere.volume(),2)))
    print("%.2f %.2f" % (round(cube.superficial_area(),2), round(cube.volume(),2)))
    print("%.2f %.2f" % (round(cuboid.superficial_area(),2),round(cuboid.volume(),2)))




