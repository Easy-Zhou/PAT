#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-09 23:40
# @Author  : zhou
# @File    : 1033 旧键盘打字
# @Software: PyCharm
# @Description:

error_l = input()
need_l = input()

for i in need_l:
    if '+' in error_l and ord('A')<=ord(i) <= ord('Z'):
        pass
    elif i.isdigit() and i in error_l:
        pass
    elif i.upper() in error_l:
        pass
    else:
        print(i,end="")
print()

