#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 08:54
# @Author  : zhou
# @File    : 1069 微博转发抽奖
# @Software: PyCharm
# @Description: 

n, step, start = map(int, input().split())
result = []
for i in range(n):
    result.append(input())

index = start
out = []
while True:
    if start > len(result):
        print('Keep going...')
        break
    if index > len(result):
        break
    if result[index - 1] in out:
        index += 1
    else:
        print(result[index - 1])
        out.append(result[index - 1])
        index += step
