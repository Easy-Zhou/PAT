#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-07 16:19
# @Author  : zhou
# @File    : 1023 组个最小数
# @Software: PyCharm
# @Description: 

list_in = [int(x) for x in input().split(" ")]

list_n = []
for i in range(10):
    for j in range(list_in[i]):
        list_n.append(i)

list_n.sort()
for i in list_n:
    if i != 0:
        list_n[list_n.index(i)] = list_n[0]
        list_n[0] = i
        break

str_n = ""
for i in list_n:
    str_n += str(i)

print(int(str_n))
