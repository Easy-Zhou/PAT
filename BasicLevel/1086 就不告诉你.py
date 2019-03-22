#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 16:36
# @Author  : zhou
# @File    : 1086 就不告诉你
# @Software: PyCharm
# @Description: 

a, b = map(int, input().split())
res = a * b
print(str(res)[::-1].lstrip('0'))