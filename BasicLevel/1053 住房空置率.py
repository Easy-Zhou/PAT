#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-17 20:41
# @Author  : zhou
# @File    : 1053 住房空置率
# @Software: PyCharm
# @Description: 

N, e, D = input().split()
N, e, D = int(N), float(e), int(D)
pro_count = 0
MS_count = 0
for i in range(N):
    temp_l = input().split()
    n = int(temp_l[0])
    t_l = [float(x) for x in temp_l[1:]]
    temp_count = 0
    for j in t_l:
        if j < e:
            temp_count += 1
    if temp_count >= n // 2 + 1:
        if n > D:
            MS_count += 1
        else:
            pro_count += 1

print('%.1f%% %.1f%%' % ((pro_count / N) * 100, (MS_count / N) * 100))
