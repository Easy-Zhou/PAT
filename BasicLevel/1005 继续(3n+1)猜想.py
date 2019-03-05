#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-03 23:02
# @Author  : zhou
# @File    : 1005 继续(3n+1)猜想
# @Software: PyCharm
# @Description:

temp = int(input())

list_num = [int(x) for x in input().split(" ")]
list_num_bak = list_num.copy()

for n in list_num:
    while True:
        if n <= 1:
            break
        elif n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n + 1) / 2

        if n in list_num_bak:
            list_num_bak.pop(list_num_bak.index(n))

list_num_bak.sort(reverse=True)
for i in list_num_bak[:-1]:
    print(i, end=" ")
print(list_num_bak[-1])
