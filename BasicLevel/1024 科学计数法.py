#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 11:18
# @Author  : zhou
# @File    : 1024 科学计数法
# @Software: PyCharm
# @Description
#
# while True:
#     s_n = input()
#     x, n = s_n.split('E')
#     l = 0
#     if '.' in x:
#         l = len(x.split('.')[1])
#     n = int(n)
#     f_n = 0
#     if n < 0:
#         f_n = l - n
#     elif 0 <= n < l:
#         f_n = l - n
#     f = '.%df' % f_n
#     print(format(float(s_n), f))


num, n = input().split('E')
x = num.split('.')
n = int(n)

s = ""
result = ""
if n <= 0:
    for i in range(len(x[0]) - 2 + n, 0, 1):
        s += '0'
    result = (s + x[0][1:] + x[1])
    result = result[0] + '.' + result[1:]
elif n > 0:
    for i in range(len(x[1]) - n, 0, 1):
        s += '0'
    if len(x[1]) - n > 0:
        result = x[0][1:] + x[1][:n] + '.' + x[1][n:]
    else:
        result = x[0][1:] + x[1] + s

if '-' in x[0]:
    print('-' + result)
else:
    print(result)
