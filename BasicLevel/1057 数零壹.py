#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 09:12
# @Author  : zhou
# @File    : 1057 数零壹
# @Software: PyCharm
# @Description: 

s = input().lower()
sum = 0
for i in s:
    if 'a' <= i <= 'z':
        sum += ord(i) - ord('a') + 1

if sum == 0:
    res = '0b'
else:
    res = bin(sum)
res = res[2:]
print(res.count('0'), res.count('1'))
