#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 16:26
# @Author  : zhou
# @File    : 1083 是否存在相等的差
# @Software: PyCharm
# @Description: 

n = int(input())
l = list(map(int, input().split()))
res_dic = {}
for i in range(n):
    minus = abs(l[i] - i - 1)
    if res_dic.get(minus) is None:
        res_dic[minus] = 1
    else:
        res_dic[minus] += 1

sorted_res = sorted(res_dic.items(), reverse=True)
for i in sorted_res:
    if i[1] > 1:
        print(i[0], i[1])
