#!/anaconda3/bin/python
# @Time    : 2019-04-03 09:38
# @Author  : zhou
# @File    : 1566学生信息输入
# @Software: PyCharm
# @Description: 


class Student:
    """学生类"""

    def __init__(self, number, name, sex, chinese, math, english):
        self.__number = number
        self.__name = name
        self.__sex = sex
        self.__chinese = chinese
        self.__math = math
        self.__english = english

    def showInfo(self):
        sum = self.__chinese + self.__math + self.__english
        ave = sum / 3
        print('%s %s %s %.2f %.2f %.2f %.2f %.2f' % (
            self.__number, self.__name, self.__sex, self.__chinese, self.__math, self.__english, ave, sum))


str_in = input().split()
str_in = [float(str_in[i]) if i > 2 else str_in[i] for i in range(len(str_in))]
student = Student(*str_in)
student.showInfo()
