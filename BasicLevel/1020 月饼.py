#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 16:13
# @Author  : zhou
# @File    : 1020 月饼
# @Software: PyCharm
# @Description: 需要使用float 使用int会出现非零返回

n, need = map(float, input().split())
stock = [float(x) for x in input().split()]
cost = [float(x) for x in input().split()]
info = []

for i in range(int(n)):
    t = (stock[i], cost[i], cost[i] / stock[i])
    info.append(t)
info = sorted(info, key=lambda x: x[2], reverse=True)

sum = 0
for i in info:
    if i[0] <= need:
        need -= i[0]
        sum += i[1]
    else:
        sum += i[1] / i[0] * need
        break

print('%.2f' % sum)
