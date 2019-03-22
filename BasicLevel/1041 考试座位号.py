#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-16 23:58
# @Author  : zhou
# @File    : 1041 考试座位号
# @Software: PyCharm
# @Description: 

n = int(input())
loc_dict = {}
for i in range(n):
    temp = input().split()
    loc_dict[temp[1]] = [temp[0],temp[2]]

m = int(input())
l = input().split()
for i in l:
    print(' '.join(loc_dict[i]))