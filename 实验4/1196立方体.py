#!/anaconda3/bin/python
# @Time    : 2019-04-04 12:09
# @Author  : zhou
# @File    : 1196立方体
# @Software: PyCharm
# @Description: 


class Cube:
    """立方体"""
    count = 0

    def __init__(self, edge):
        self.__edge = edge
        self.__volume = self.calVolume()
        self.__area = self.calArea()
        Cube.count += 1

    def calVolume(self):
        """计算立方体体积"""
        return round(self.__edge ** 3, 2)

    def calArea(self):
        """计算立方体表面积"""
        return round(self.__edge ** 2 * 6, 2)

    def display(self):
        """输出"""
        print('obj%d Volume:%.2f; Area:%.2f' % (Cube.count, self.__volume, self.__area))


n = int(input())
for i in range(n):
    edge = float(input())
    cube = Cube(edge)
    cube.display()
