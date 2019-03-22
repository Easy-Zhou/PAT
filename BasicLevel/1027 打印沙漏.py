#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 16:51
# @Author  : zhou
# @File    : 1027 打印沙漏
# @Software: PyCharm
# @Description: 

n, sign = input().split()
n = int(n)
l = []
count = 1
sum_t = 1
rest = 0
while True:
    temp = ''
    for j in range(count):
        temp += sign
    l.append(temp)
    count += 2
    if (sum_t + count) * 2 - 1 > n:
        rest = n - sum_t * 2 + 1
        break
    sum_t += count

for i in range(len(l) - 1, 0, -1):
    for j in range(len(l) - 1 - i):
        print(' ', end='')
    print(l[i])
for i in range((len(l[len(l)-1])-1)//2):
    print(' ',end='')
print(l[0])
for i in range(1, len(l), 1):
    for j in range(len(l) - 1 - i):
        print(' ', end='')
    print(l[i])
print(rest)
