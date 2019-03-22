#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-20 10:22
# @Author  : zhou
# @File    : 1064 朋友数
# @Software: PyCharm
# @Description:

n = int(input())
num_l = input().split()

result_set = set()
for i in num_l:
    sum_t = 0
    for j in i:
        sum_t += int(j)
    result_set.add(sum_t)

print(len(result_set))

print(' '.join([str(x) for x in sorted(result_set)]))
