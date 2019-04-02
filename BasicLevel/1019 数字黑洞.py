#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-24 23:36
# @Author  : zhou
# @File    : 1019 数字黑洞
# @Software: PyCharm
# @Description: 

num_l = list(input().rjust(4,'0'))

a = ''.join(sorted(num_l, reverse=True))
b = ''.join(sorted(num_l))
if a[0] == a[3]:
    print(a, '-', b, '= 0000')
    exit()
while True:
    difference = int(a) - int(b)
    str_difference = str(difference).rjust(4,'0')
    print(a, '-', b, '=', str_difference)
    str_difference = list(str_difference)
    if difference == 6174:
        break
    a = ''.join(sorted(str_difference, reverse=True))
    b = ''.join(sorted(str_difference))

