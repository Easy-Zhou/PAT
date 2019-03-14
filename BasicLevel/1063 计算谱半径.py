#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 09:35
# @Author  : zhou
# @File    : 1063 计算谱半径
# @Software: PyCharm
# @Description: 

import math

n = int(input())
m = 0
for i in range(n):
    a, b = map(int, input().split())
    tmp = math.sqrt(a * a + b * b)
    if tmp > m:
        m = tmp

print('%.2f' % m)
