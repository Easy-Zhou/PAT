#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 16:09
# @Author  : zhou
# @File    : 1079 延迟的回文数
# @Software: PyCharm
# @Description: 

s = input()

for i in range(10):
    if s == s[::-1]:
        print(s + ' is a palindromic number.')
        break
    else:
        pa = s[::-1]
        t = str(int(s) + int(pa))
        print("%s + %s = %s" % (s, pa, t))
        s = t
else:
    print('Not found in 10 iterations.')
