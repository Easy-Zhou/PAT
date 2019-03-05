#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-03 22:52
# @Author  : zhou
# @File    : 1076 Wifi密码
# @Software: PyCharm
# @Description: 

n = int(input())

str_list = []
for i in range(n):
    str_list.append(input().split(" "))

for i in range(len(str_list)):
    if "A-T" in str_list[i]:
        print(1,end="")
    elif "B-T" in str_list[i]:
        print(2,end="")
    elif "C-T" in str_list[i]:
        print(3,end="")
    elif "D-T" in str_list[i]:
        print(4,end="")

print()