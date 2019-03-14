#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 12:07
# @Author  : zhou
# @File    : 1071 小赌怡情
# @Software: PyCharm
# @Description: 

To, n = map(int, input().split())
for i in range(n):
    n1,b,t,n2 = map(int, input().split())
    if t > To:
        print('Not enough tokens.  Total = %d.'%To)
    elif b == 0 and n2 < n1:
        To += t
        print('Win %d!  Total = %d.'%(t,To))
    elif b == 1 and n2 > n1:
        To += t
        print('Win %d!  Total = %d.'%(t,To))
    else:
        To -= t
        print('Lose %d.  Total = %d.'%(t,To))
        if To == 0:
            print('Game Over.')
            break

