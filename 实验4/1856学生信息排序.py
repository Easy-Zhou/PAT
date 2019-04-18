#!/anaconda3/bin/python
# @Time    : 2019-04-04 12:48
# @Author  : zhou
# @File    : 1856学生信息排序
# @Software: PyCharm
# @Description: 


class Student:
    """学生类"""

    def __init__(self, id, name, sex, chinese, math, english):
        self.__id = id
        self.__name = name
        self.__sex = sex
        self.__chinese = chinese
        self.__math = math
        self.__english = english
        self.__chinese = float(chinese)
        self.__math = float(math)
        self.__english = float(english)
        self.__sum = (self.__chinese + self.__math + self.__english)
        self.__ave = self.__sum / 3


    @property
    def id(self):
        return self.__id

    def showInfo(self):
        print(self.__id, self.__name, self.__sex,
              " %.2f %.2f %.2f %.2f %.2f" % (self.__chinese, self.__math, self.__english, self.__ave, self.__sum))


class SortStudent:
    """学生信息排序"""

    student = []

    @classmethod
    def quit(cls):
        print("Good bye!")
        exit(0)

    @classmethod
    def insert(cls, *args):
        for stu in cls.student:
            if stu.id == args[0]:
                print('Failed')
                break
        else:
            s = Student(*args)
            cls.student.append(s)
            s.showInfo()

    @classmethod
    def list(cls):
        for stu in cls.student:
            stu.showInfo()


while True:
    str_in = input().split()
    cmd = str_in[0]
    str_in = str_in[1:]
    if hasattr(SortStudent, cmd.lower()):
        func = getattr(SortStudent, cmd.lower())
        func(*str_in)
