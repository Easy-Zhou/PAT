#!/anaconda3/bin/python
# @Time    : 2019-04-17 20:06
# @Author  : zhou
# @File    : OPP
# @Software: PyCharm
# @Description: 


class get_set_test:
    """

    """
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name


te = get_set_test("tt",12)

print(te.name)
te.name = "ps"
print(te.name)