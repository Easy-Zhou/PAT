#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 17:31
# @Author  : zhou
# @File    : 1088 三人行
# @Software: PyCharm
# @Description: 


M, X, Y = map(int, input().split())
max = 0
res_out = []
temp = []
for i in range(10, 100, 1):
    A = i
    B = int(str(i)[::-1])
    C = abs(B - A) / X
    if B == C * Y:
        max = A
        temp = [A, B, C]

if max != 0:
    print(max, end=' ')
    for i in range(len(temp)):
        if temp[i] > M:
            print('Cong', end='')
        elif temp[i] == M:
            print('Ping', end='')
        else:
            print('Gai', end='')
        if i != len(temp) - 1:
            print(' ', end='')
    print()

else:
    print('No Solution')
