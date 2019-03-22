#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-20 10:33
# @Author  : zhou
# @File    : 1065 单身狗
# @Software: PyCharm
# @Description: 

n = int(input())

couple_dic = []
for i in range(n):
    couple_dic.append(input().split())

input()
customer = set(input().split())
for j in couple_dic:
    if j[0] in customer and j[1] in customer:
        customer.remove(j[0])
        customer.remove(j[1])

print(len(customer))
customer = list(customer)
customer.sort()
if len(customer) != 0:
    print(' '.join(customer))