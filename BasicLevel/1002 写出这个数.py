#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 16:04
# @Author  : zhou
# @File    : 1002 写出这个数
# @Software: PyCharm
# @Description: 

pinyin = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu", "shi"]
n = input()
sum = 0
for i in range(len(n)):
    sum += int(n[i])

L = []
while sum != 0:
    L.append(sum % 10)
    sum //= 10

L.reverse()

for i in range(len(L)):
    if i == len(L) - 1:
        print(pinyin[L[i]])
    else:
        print(pinyin[L[i]], end=" ")
