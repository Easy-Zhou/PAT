#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-28 16:51
# @Author  : zhou
# @File    : 1070 结绳
# @Software: PyCharm
# @Description: 

import math
n = input()
string_len = list(map(int, input().split()))
string_len.sort()
left = string_len[0]
for i in string_len[1:]:
    left = (left + i)/2

print(math.floor(left))
