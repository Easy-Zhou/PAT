#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 09:04
# @Author  : zhou
# @File    : 1056 组合数的和
# @Software: PyCharm
# @Description: 

l = input().split()
res = []
for i in l[1:]:
    for j in l[1:]:
        if i != j and i+j not in res:
            res.append(i+j)
sum = 0
for i in res:
    sum += int(i)

print(sum)