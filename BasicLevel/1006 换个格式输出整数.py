#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-03 23:48
# @Author  : zhou
# @File    : 1006 换个格式输出整数
# @Software: PyCharm
# @Description: 

n = int(input())
tag = ['B', 'S']
L = []
while n > 0:
    L.append(n % 10)
    n //= 10

if len(L) == 2:
    L.append(0)

elif len(L) == 1:
    L.append(0)
    L.append(0)

L.reverse()

for i in range(len(L)):
    for j in range(L[i]):
        if i == 2:
            print(j + 1, end="")
        else:
            print(tag[i], end="")

print()
