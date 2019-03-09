#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 08:38
# @Author  : zhou
# @File    : 1016 部分A+B
# @Software: PyCharm
# @Description:

a, da, b, db = input().split(" ")

countA = a.count(da)
countB = b.count(db)

if da in a:
    pa = da
else:
    pa = 0
if db in b:
    pb = db
else:
    pb = 0
# for i in range(countA):
#     pa += da
#
# for i in range(countB):
#     pb += db

print(int(pa*countA)+int(pb*countB))





