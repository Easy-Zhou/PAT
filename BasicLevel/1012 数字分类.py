#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 20:46
# @Author  : zhou
# @File    : 1012 数字分类
# @Software: PyCharm
# @Description:

n_list = [int(x) for x in input().split(" ")]

sum_a1 = 0
sum_a2 = 0
count_a3 = 0
count_a4 = 0
sum_a4 = 0
list_a5 = []
flag = 1
result = ['N', 'N', 'N', 'N', 'N']
for i in range(1, len(n_list)):
    if n_list[i] % 10 == 0:
        sum_a1 += n_list[i]
        result[0] = sum_a1
    elif n_list[i] % 5 == 1:
        if flag == 1:
            sum_a2 += n_list[i]
            flag = 0
        else:
            sum_a2 -= n_list[i]
            flag = 1
        result[1] = sum_a2
    elif n_list[i] % 5 == 2:
        count_a3 += 1
        result[2] = count_a3
    elif n_list[i] % 5 == 3:
        count_a4 += 1
        sum_a4 += n_list[i]
        result[3] = sum_a4 / count_a4
    elif n_list[i] % 5 == 4:
        list_a5.append(n_list[i])
        result[4] = max(list_a5)

for i in result[:3]:
    print(i, end=" ")
if result[3] != 'N':
    print("%.1f" % result[3], result[4])
else:
    print(result[3], result[4])
