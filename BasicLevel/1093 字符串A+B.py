#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-22 14:30
# @Author  : zhou
# @File    : 1093 字符串A+B
# @Software: PyCharm
# @Description: 

A = input()
B = input()
a_set = set(A + B)
for i in A + B:
    if i in a_set:
        print(i, end='')
        a_set.remove(i)
print()
