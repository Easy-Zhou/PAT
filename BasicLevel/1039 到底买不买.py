#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-16 22:32
# @Author  : zhou
# @File    : 1039 到底买不买
# @Software: PyCharm
# @Description: 

have = input()
need = input()

have_dic = {}
need_dic = {}

for i in have:
    if i not in have_dic:
        have_dic[i] = 1
    else:
        have_dic[i] += 1

for i in need:
    if i not in need_dic:
        need_dic[i] = 1
    else:
        need_dic[i] += 1

for key, value in need_dic.items():
    if key in have_dic.keys():
        have_dic[key] -= value
    else:
        have_dic[key] = -value

lack = 0
enough = 0
for value in have_dic.values():
    if value < 0:
        lack += abs(value)
    else:
        enough += value

if lack > 0:
    print('No', lack)
else:
    print('Yes', enough)
