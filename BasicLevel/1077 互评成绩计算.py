#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-26 01:52
# @Author  : zhou
# @File    : 1077 互评成绩计算
# @Software: PyCharm
# @Description: 

import math

n,top_score = map(int,input().split())
for i in range(n):
    temp_score_list = list(map(int, input().split()))
    sum = 0
    count = 0
    score_list = []
    for j in temp_score_list[1:]:
        if j > top_score or j < 0:
            pass
        else:
            score_list.append(j)
    score_list.remove(max(score_list))
    score_list.remove(min(score_list))
    ave = math.fsum(score_list) / len(score_list)
    print(format(round((ave+temp_score_list[0])/2+0.01 ),'d'))





