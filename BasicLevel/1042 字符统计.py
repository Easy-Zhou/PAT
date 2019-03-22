#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-17 00:12
# @Author  : zhou
# @File    : 1042 字符统计
# @Software: PyCharm
# @Description: 

import re
in_str = input().lower()
in_str = re.findall('[a-z]',in_str)
res_dic = {}
for i in in_str:
    if i in res_dic.keys():
        res_dic[i] += 1
    else:
        res_dic[i] = 1

# key = max(res_dic, key=res_dic.get)
Mx = ['a',0]
for k,v in res_dic.items():
    if v > Mx[1] or (v == Mx[1] and ord(k) < ord(Mx[0])):
        Mx[0] = k
        Mx[1] = v
print(Mx[0],Mx[1])
