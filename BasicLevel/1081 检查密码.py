#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 12:18
# @Author  : zhou
# @File    : 1081 检查密码
# @Software: PyCharm
# @Description: 

n = int(input())
num = ''
wo = ''
sign = '.'
for i in range(10):
    num += str(i)
for i in range(ord('a'),ord('z')+1):
    wo += chr(i)
    wo += chr(i).upper()
for i in range(n):
    pwd = input()
    num_flag = 0
    wo_flag = 0
    len_flag = 0
    l = len(pwd)
    if len(pwd) < 6:
        print('Your password is tai duan le.')
    else:
        for j in pwd:
            if j not in num and j not in wo and j not in sign:
                print('Your password is tai luan le.')
                len_flag = 1
                break
            elif j in num:
                num_flag = 1
            elif j in wo:
                wo_flag = 1
        if len_flag == 0:
            if num_flag == 1 and wo_flag == 1:
                print('Your password is wan mei.')
            elif num_flag == 1 and wo_flag == 0:
                print('Your password needs zi mu.')
            elif num_flag == 0 and wo_flag == 1:
                print('Your password needs shu zi.')


# 5
# 123s
# zheshi.wodepw
# 1234.5678
# WanMei23333
# pass*word.6
