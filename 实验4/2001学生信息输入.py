#!/anaconda3/bin/python
# @Time    : 2019-04-04 00:19
# @Author  : zhou
# @File    : 2001学生信息输入
# @Software: PyCharm
# @Description: 


class Student:
    """学生类"""

    def __init__(self, id, name, sex, year, month, day, x, y, z):
        self.__id = id
        self.__name = name
        self.__sex = sex
        self.__year = year
        self.__month = month
        self.__day = day
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.__sum = (self.__x + self.__y + self.__z)
        self.__ave = self.__sum / 3

    @property
    def id(self):
        return self.__id

    @property
    def sum(self):
        return self.__sum

    @property
    def birthday(self):
        return self.__year + self.__month + self.__day

    def showInfo(self):
        print(self.__id, self.__name, self.__sex, self.__year, self.__month,
              self.__day + " %.1f %.1f %.1f %.1f %.1f" % (self.__x, self.__y, self.__z, self.__ave, self.__sum))

    def change(self, name, sex, year, month, day, x, y, z):
        self.__name = name
        self.__sex = sex
        self.__year = year
        self.__month = month
        self.__day = day
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.__sum = (self.__x + self.__y + self.__z)
        self.__ave = self.__sum / 3


class Manage:
    """学生信息管理类"""
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
    def change(cls, *args):
        for stu in cls.student:
            if stu.id == str:
                stu.change(*args)
                stu.showInfo()

    @classmethod
    def delete(cls, id):
        for stu in cls.student:
            if stu.id == id:
                cls.student.remove(stu)
        print("Deleted")

    @classmethod
    def find(cls, id):
        for stu in cls.student:
            if stu.id == id:
                stu.showInfo()
                break
        else:
            print("Failed")

    @classmethod
    def sort(cls, cmd):
        if cmd == 'byid':
            cls.student.sort(key=lambda x: x.id)
            for stu in cls.student:
                stu.showInfo()
        elif cmd == 'bybirthday':
            cls.student.sort(key=lambda x: x.birthday)
            for stu in cls.student:
                stu.showInfo()
        elif cmd == 'bysum':
            cls.student.sort(key=lambda x: x.sum)
            for stu in cls.student:
                stu.showInfo()


while True:
    str_in = input().split()
    cmd = str_in[0]
    str_in = str_in[1:]
    if hasattr(Manage, cmd.lower()):
        print(cmd + ':')
        func = getattr(Manage, cmd.lower())
        func(*str_in)
