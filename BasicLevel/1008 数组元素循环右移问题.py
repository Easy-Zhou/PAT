#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 09:00
# @Author  : zhou
# @File    : 1008 数组元素循环右移问题
# @Software: PyCharm
# @Description: 

l, n = map(int, input().split(" "))
n_list = [int(x) for x in input().split(" ")]

if n == 0 or n == l or l == 1 or n % l == 0:
    result_list = n_list
else:
    if n > l:
        n = n % l

    result_list = n_list[-n:]
    result_list.extend(n_list[:l - n])
for x in result_list[:-1]:
    print(x, end=" ")
print(result_list[-1])
