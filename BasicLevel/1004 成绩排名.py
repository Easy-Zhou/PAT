#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-03 22:17
# @Author  : zhou
# @File    : 1004 成绩排名
# @Software: PyCharm
# @Description: 

n = int(input())
grade_list = []
for i in range(n):
     temp = input().split(" ")
     grade_list.append([temp[0],temp[1],int(temp[2])])

grade_list = sorted(grade_list,key=lambda x:(x[2]))

print(grade_list[-1][0],grade_list[-1][1])
print(grade_list[0][0],grade_list[0][1])

