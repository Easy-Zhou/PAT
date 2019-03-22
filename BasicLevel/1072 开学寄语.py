#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-17 00:56
# @Author  : zhou
# @File    : 1072 开学寄语
# @Software: PyCharm
# @Description: 

stu_n, pro_n = map(int, input().split())
pro = input().split()
stu_count, pro_count = 0, 0
for i in range(stu_n):
    stu_pro = input().split()
    stu_flag = 0
    out_str = ''
    for p in stu_pro:
        if p in pro and stu_flag == 1:
            out_str += p + " "
            pro_count += 1
        elif p in pro and stu_flag == 0:
            out_str += stu_pro[0] + ': ' + p + " "
            stu_flag = 1
            stu_count += 1
            pro_count += 1
    if stu_flag == 1:
        print(out_str.rstrip())
print(stu_count,pro_count)

