#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-20 08:17
# @Author  : zhou
# @File    : 1058 选择题
# @Software: PyCharm
# @Description: 

n, m = map(int, input().split())
correct_ans = []
score = []
for i in range(m):
    temp_str = input()
    ans_t = '(' + temp_str[4:]
    correct_ans.append(ans_t)
    score.append(int(temp_str[0]))

ans_l = []
wrong_count = [0] * m
for i in range(n):
    ans_l.clear()
    ans = input()
    temp = ''
    stu_score = 0
    # for j in ans:
    #     if j == '(':
    #         temp = ''
    #     elif j == ')':
    #         ans_l.append(temp)
    #     else:
    #         temp += j

    ans_l = [x.lstrip() for x in ans.split(')')][:-1]

    for j in range(len(ans_l)):
        if ans_l[j] == correct_ans[j]:
            stu_score += score[j]
        else:
            wrong_count[j] += 1
    print(stu_score)

if max(wrong_count) == 0:
    print('Too simple')
else:
    print(max(wrong_count), end=' ')
    index = ''
    for i in range(len(wrong_count)):
        if wrong_count[i] == max(wrong_count):
            index += (str(i + 1) + ' ')
    print(index.rstrip())
