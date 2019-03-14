#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 08:18
# @Author  : zhou
# @File    : 1051 复数乘法
# @Software: PyCharm
# @Description: 

import math

r1, p1, r2, p2 = map(float, input().split())
c1 = complex(r1 * math.cos(p1), r1 * math.sin(p1))
c2 = complex(r2 * math.cos(p2), r2 * math.sin(p2))
c = c1 * c2
re1 = '%.2f' % c.real
re2 = '+%.2fi' % abs(c.imag)

if float(format(c.real, '.2f')) == 0 and c.real < 0:
    re1 = '%.2f' % abs(c.real)
if float(format(c.imag, '.2f')) < 0:
    re2 = '-%.2fi' % abs(c.imag)
print(re1 + re2)
