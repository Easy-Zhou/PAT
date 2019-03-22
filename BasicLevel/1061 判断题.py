#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-20 10:12
# @Author  : zhou
# @File    : 1061 判断题
# @Software: PyCharm
# @Description: 

n,m = map(int,input().split())

score = list(map(int,input().split()))
correct = input().split()


for i in range(n):
    stu_score = 0
    ans = input().split()
    for j in range(len(ans)):
        if ans[j] == correct[j]:
            stu_score += score[j]

    print(stu_score)