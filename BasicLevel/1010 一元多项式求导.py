#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 15:51
# @Author  : zhou
# @File    : 1010 一元多项式求导
# @Software: PyCharm
# @Description: 若只有零式多项式(n*x**0)需要输出0 0

list_in = [int(x) for x in input().split()]
result = []
for i in range(0, len(list_in), 2):
    if list_in[i] == 0 or list_in[i + 1] == 0:
        if i == 0:
            result.append(0)
            result.append(0)
    else:
        result.append(list_in[i] * list_in[i + 1])
        result.append(list_in[i + 1] - 1)
print(' '.join([str(x) for x in result]))
