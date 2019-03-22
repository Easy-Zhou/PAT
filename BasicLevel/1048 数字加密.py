#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-17 19:16
# @Author  : zhou
# @File    : 1048 数字加密
# @Software: PyCharm
# @Description: 

A, B = input().split()
A = A.rjust(max(len(A), len(B)), '0')
B = B.rjust(max(len(A), len(B)), '0')
A = list(A)
B = list(B)

A.reverse()
B.reverse()
sign = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
result = []
for i in range(len(A)):
    if i % 2 == 0:
        t = (int(A[i]) + int(B[i])) % 13
        result.append(sign[t])
    else:
        t = (int(B[i]) - int(A[i]))
        if t < 0:
            t += 10
        result.append(str(t))
result.reverse()
print(''.join(result))
