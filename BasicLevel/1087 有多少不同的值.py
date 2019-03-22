#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 16:42
# @Author  : zhou
# @File    : 1087 有多少不同的值
# @Software: PyCharm
# @Description: 

import math

n = int(input())
res = set()
for i in range(n+1):
    ans = math.floor(i/2) + math.floor(i/3) + math.floor(i/5)
    res.add(ans)

print(len(res))

