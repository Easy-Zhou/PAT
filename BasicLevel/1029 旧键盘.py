#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 23:34
# @Author  : zhou
# @File    : 1029 旧键盘
# @Software: PyCharm
# @Description: 

str_in = input().upper()
str_out = input().upper()
str_err = ''
for i in str_in:
    if i not in str_out and i not in str_err:
        str_err += i
print(str_err)