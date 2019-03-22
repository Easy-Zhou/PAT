#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-17 00:43
# @Author  : zhou
# @File    : 1043 输出PATest
# @Software: PyCharm
# @Description: 

in_str = input()
str_dic = {}
PATest = 'PATest'
for i in PATest:
    str_dic[i] = 0
for i in in_str:
    if i in PATest:
        str_dic[i] += 1

res = ''
while True:
    res_t = ''
    for i in PATest:
        if str_dic[i] > 0:
            res_t += i
            str_dic[i] -= 1
    if len(res_t) == 0:
        break
    res += res_t
print(res)

