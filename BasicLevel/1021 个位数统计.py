#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 10:36
# @Author  : zhou
# @File    : 1021 个位数统计
# @Software: PyCharm
# @Description: 

a = input()
dic = {}
for i in a:
    dic[i] = str(a.count(i))

result = sorted(dic.items())
for i in result:
    print(':'.join(i))
