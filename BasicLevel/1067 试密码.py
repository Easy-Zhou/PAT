#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 09:40
# @Author  : zhou
# @File    : 1067 试密码
# @Software: PyCharm
# @Description: 

pwd, n = input().split()
n = int(n)
flag = 0
count = 0
for i in range(n):
    pwd_in = input()
    if pwd_in == '#':
        flag = 1
        break
    elif pwd_in == pwd:
        print('Welcome in')
        flag = 1
        break
    else:
        print('Wrong password:', pwd_in)

if flag == 0:
    print("Account locked")