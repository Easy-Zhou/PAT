#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-07 16:46
# @Author  : zhou
# @File    : 1026 程序运行时间
# @Software: PyCharm
# @Description: 


start_time, end_time = map(int, input().split(" "))

spend_time = round((end_time - start_time) / 100)

m, s = divmod(spend_time, 60)
h, m = divmod(m, 60)

print("%02d:%02d:%02d" % (h, m, s))
