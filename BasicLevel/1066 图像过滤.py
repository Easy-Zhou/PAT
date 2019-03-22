#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-20 22:06
# @Author  : zhou
# @File    : 1066 图像过滤
# @Software: PyCharm
# @Description: 

import RunTime_z


@RunTime_z.Time
def ttt():
    """

    :return:
    """
    n, m, a, b, r = map(int, input().split())
    r = str(r)
    for k in range(n):
        in_l = input().split()
        for i in range(m):
            if a <= int(in_l[i]) <= b:
                in_l[i] = "0" * (3 - len(r)) + r
            else:
                in_l[i] = "0" * (3 - len(in_l[i])) + in_l[i]
        print(' '.join(in_l))

    ################################################
    # M, N, A, B, f = input().split()
    # M = int(M)
    # N = int(N)
    # A = int(A)
    # B = int(B)
    # for i in range(M):
    #     tem_l = input().split()
    #     for j in range(N):
    #         if A <= int(tem_l[j]) <= B:
    #             tem_l[j] = "0" * (3 - len(f)) + f
    #         else:
    #             tem_l[j] = "0" * (3 - len(tem_l[j])) + tem_l[j]
    #     print(" ".join(tem_l))


ttt()
