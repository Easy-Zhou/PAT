#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 16:27
# @Author  : zhou
# @File    : 1003 我要通过
# @Software: PyCharm
# @Description: 

PAT=['P','A','T']
a,b,c="","",""
n = int(input())

for i in range(n):
    in_string = input()
    for j in range(len(in_string)):
        if in_string[i] not in PAT:
            print('NO')
        elif in_string != "P":
            a += in_string[j]
        else:
            pass


