#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-15 00:03
# @Author  : zhou
# @File    : 1031 查验身份证
# @Software: PyCharm
# @Description: 

a = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
M = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
n = int(input())
result = []
for i in range(n):
    Id = input()
    sum = 0
    flag = 0
    for j in range(17):
        if Id[j].isdigit():
            sum += int(Id[j]) * a[j]
        else:
            flag = 1
            break
    temp = sum % 11
    if M[int(temp)] == Id[-1] and flag == 0:
        result.append(Id)
    else:
        print(Id)
if len(result) == n:
    print('All passed')
