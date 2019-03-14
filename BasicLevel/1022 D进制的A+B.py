#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 10:53
# @Author  : zhou
# @File    : 1022 D进制的A+B
# @Software: PyCharm
# @Description: 
a, b, c = map(int, input().split())

s = a + b

result = ''
while True:
    s, r = divmod(s, c)
    result += str(r)
    if s == 0:
        break

result = list(result)
result.reverse()
for i in result:
    print(i,end="")
print()
