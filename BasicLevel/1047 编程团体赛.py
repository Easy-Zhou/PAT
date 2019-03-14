#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 09:47
# @Author  : zhou
# @File    : 1047 编程团体赛
# @Software: PyCharm
# @Description:

n = int(input())
result = [0] * 1001
for i in range(n):
    a, b = input().split()
    result[int(a.split('-')[0])] += int(b)

print(result.index(max(result)), max(result))
