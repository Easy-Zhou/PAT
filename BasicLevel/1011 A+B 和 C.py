#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 08:50
# @Author  : zhou
# @File    : 1011 A+B 和 C
# @Software: PyCharm
# @Description: 

a = int(input())
for i in range(a):
    b, c, d = map(int, input().split())
    print("Case #"+str(i+1)+": true" if b+c > d else "Case #"+str(i+1)+": false")
