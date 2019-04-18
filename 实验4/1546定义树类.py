#!/anaconda3/bin/python
# @Time    : 2019-04-03 09:14
# @Author  : zhou
# @File    : 1546定义树类
# @Software: PyCharm
# @Description: 


class Tree:
    """树类🌲"""

    def __init__(self, age):
        self.__age = age

    def grow(self, years):
        self.__age += years

    def showAge(self):
        print("Tree ages:" + str(self.__age))


while True:
    age, years = map(int, input().split())
    if age == 0 and years == 0:
        break
    else:
        tree = Tree(age)
        tree.grow(years)
        tree.showAge()
