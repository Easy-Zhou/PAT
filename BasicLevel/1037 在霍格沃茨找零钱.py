#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 19:05
# @Author  : zhou
# @File    : 1037 在霍格沃茨找零钱
# @Software: PyCharm
# @Description:

P, A = input().split(' ')
P = [int(x) for x in P.split('.')]
A = [int(x) for x in A.split('.')]

sign = ''
for i in range(3):
    if A[i] < P[i]:
        sign = '-'
        temp = P.copy()
        P = A.copy()
        A = temp.copy()
        break
    elif A[i] > P[i]:
        break
    else:
        continue

result = []
for i in range(3):
    result.append(A[i] - P[i])

if result[2] < 0:
    result[2] = result[2] + 29
    result[1] -= 1
if result[1] < 0:
    result[1] = result[1] + 17
    result[0] -= 1

print(sign + str(result[0]) + '.' + str(result[1]) + '.' + str(result[2]))
