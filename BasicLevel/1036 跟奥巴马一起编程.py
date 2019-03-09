#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-07 18:22
# @Author  : zhou
# @File    : 1036 跟奥巴马一起编程
# @Software: PyCharm
# @Description: 

import math
n, c = input().split(" ")
n = int(n)
m = math.ceil(n/2)
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            print(c, end="")
        else:
            print(' ', end="")
    print()
