#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 09:42
# @Author  : zhou
# @File    : 1082 射击比赛
# @Software: PyCharm
# @Description: 

n = int(input())
d = {}
for i in range(n):
    pid, x, y = input().split()
    d[pid] = (int(x) ** 2 + int(y) ** 2)

print(min(d, key=d.get), max(d, key=d.get))
