#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 15:34
# @Author  : zhou
# @File    : 1078 字符串压缩与解压
# @Software: PyCharm
# @Description: 


sign = input()
if sign == 'C':
    str_in = input()+'0'
    rem = ''
    count = 1
    for i in str_in:
        if rem != i:
            if count != 1:
                print(str(count) + rem, end='')
            else:
                print(rem, end='')
            rem = i
            count = 1
        elif rem == i:
            count += 1
elif sign == 'D':
    unzip_str_in = input()
    unzip_count = 1
    str_count = ''
    for i in range(len(unzip_str_in)):
        if unzip_str_in[i].isdigit():
            str_count += unzip_str_in[i]
        else:
            if len(str_count) > 0:
                unzip_count = int(str_count)
                str_count = ''
                for j in range(unzip_count):
                    print(unzip_str_in[i],end='')
            else:
                print(unzip_str_in[i],end='')

print()
