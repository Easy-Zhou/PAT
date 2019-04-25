#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-18 17:50
# @Author  : zhou
# @File    : 1055 集体照
# @Software: PyCharm
# @Description: 
import math

n, k = map(int, input().split())
stu = []
for i in range(n):
    stu_temp = tuple([float(i) if i.isdigit() else i for i in input().split()])
    stu.append(stu_temp)

stu = sorted(stu, key=lambda x: (-x[1], x[0]),reverse=True)
step = n // k
result = []
for i in range(k):
    if i == k - 1:
        temp = stu[i * step:]
    else:
        temp = stu[i * step:(i + 1) * step]
    temp.reverse()
    result.insert(0, temp)

for i in result:
    l = len(i)
    order = [0] * l
    index = l // 2
    count = 1
    for j in range(l):
        order[index] = j
        index += (-1) ** (j + 1) * count
        count += 1
    for j in order[:-1]:
        print(i[j][0],end=' ')
    print(i[order[-1]][0])