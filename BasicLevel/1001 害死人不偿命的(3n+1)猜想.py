#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 15:49
# @Author  : zhou
# @File    : 1001 害死人不偿命的(3n+1)猜想
# @Software: PyCharm
# @Description:

n = int(input())
count = 0
while True:
    if n <= 1:
        break
    elif n % 2 == 0:
        n = n / 2
    else:
        n = (3 * n + 1) / 2
    count += 1

print(count)
