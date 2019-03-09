#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-07 16:10
# @Author  : zhou
# @File    : 1014 福尔摩斯的约会
# @Software: PyCharm
# @Description: 

# print(chr(97))
# print(ord("A"))
# print(ord('0'))
weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
l = []
for i in range(4):
    l.append(input())
flag = 0
for i in range(min(len(l[0]), len(l[1]))):
    if l[0][i] == l[1][i]:
        if flag == 0 and ord('A') <= ord(l[0][i]) <= ord('G'):
            print(weekday[ord(l[0][i]) - ord('A')], end=" ")
            flag = 1
        elif flag == 1 and ord('0') <= ord(l[0][i]) <= ord('9'):
            print('%02d:' % (ord(l[0][i]) - ord('0')), end="")
            break
        elif flag == 1 and ord('A') <= ord(l[0][i]) <= ord('N'):
            print('%02d:' % (ord(l[0][i]) - ord('A') + 10), end="")
            break

for i in range(min(len(l[2]), len(l[3]))):
    if l[2][i] == l[3][i] and (ord('A') <= ord(l[2][i]) <= ord('Z') or ord('a') <= ord(l[2][i]) <= ord('z')):
        print('%02d' % i)
        break
