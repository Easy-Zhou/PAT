#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 08:30
# @Author  : zhou
# @File    : 1017 A除以B
# @Software: PyCharm
# @Description: 

a, b = [int(x) for x in input().split(" ")]  # 拆包
# a,b = map(int,input().split(" ")
print(a // b, a % b)
