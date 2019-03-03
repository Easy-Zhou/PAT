#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-03 14:34
# @Author  : zhou
# @File    : 1091 N-自守数
# @Software: PyCharm
# @Description:

n = int(input())
s = input()

L = [int(x) for x in s.split(" ")]

for i in range(len(L)):
    num_len = len(str(L[i]))
    temp = 10**num_len
    for j in range(10):
        if j*L[i]**2%temp == L[i]:
            print(j,j*L[i]**2)
            break
        elif j==9:
            print("No")

