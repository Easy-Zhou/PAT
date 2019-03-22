#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-15 16:49
# @Author  : zhou
# @File    : 1038 统计同成绩学生
# @Software: PyCharm
# @Description: 

import time
import numpy as np


def Time(func):
    """
    用于计算函数运行时间的装饰器
    :param func:
    :return:
    """

    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("运行时间：", end_time - start_time)

    return deco


@Time
def str_fun(stu_grade, same_grade):
    result = []
    for i in same_grade:
        result.append(str(stu_grade.count(i)))
    print(' '.join(result))


@Time
def list_fun(stu_grade, same_grade):
    stu_grade = stu_grade.split()
    result = []
    for i in same_grade:
        result.append(str(stu_grade.count(i)))
    print(' '.join(result))


@Time
def np_fun(stu_grade, same_grade, n):
    stu_grade = np.array(stu_grade.split())
    # result= np.zeros(([5,]),int)
    same_grade = np.array(same_grade)
    for i in same_grade:
        print(np.sum(stu_grade == i), end=" ")
        # np.append(result,np.sum(stu_grade==i))
    # for i in result:
    #     print(i,end=' ')


@Time
def loop_all(in_str):
    """

    :param in_str:
    :return:
    """
    ans_l = []
    temp = ''
    for j in in_str:
        if j == '(':
            temp = ''
        elif j == ')':
            ans_l.append(temp)
        else:
            temp += j


@Time
def split_t(in_str):
    """

    :param in_str:
    :return:
    """
    ans_l = [x.lstrip() for x in in_str.split()]


a = input()
loop_all(a)
split_t(a)

n = input()
stu_grade = input().split()
same_grade = input().split()
result = {}
out = []
for i in same_grade[1:]:
    result[i] = 0
for i in stu_grade:
    if i in result:
        result[i] += 1
for i in same_grade[1:]:
    out.append(str(result[i]))
print(' '.join(out))
# stu_grade *= 10000
# same_grade.extend(['60','55','99','65','50','1','2','3','10','11'])

str_fun(stu_grade, same_grade)
list_fun(stu_grade, same_grade)
np_fun(stu_grade, same_grade, m)
