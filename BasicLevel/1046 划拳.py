#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 23:31
# @Author  : zhou
# @File    : 1046 划拳
# @Software: PyCharm
# @Description: 

n = int(input())

result = [0,0]
for i in range(n):
    temp = [int(x) for x in input().split(" ")]
    r_sum = temp[0] + temp[2]
    if r_sum== temp[1] and r_sum != temp[3]:
        result[1] += 1
    elif r_sum != temp[1] and  r_sum== temp[3]:
        result[0] += 1
print(result[0],result[1])