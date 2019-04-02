#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-22 14:51
# @Author  : zhou
# @File    : 1007 素数对猜想
# @Software: PyCharm
# @Description:

import math


def isPrime(num):
    """

    :return: True or False tu judge isPrime number
    """
    if num <= 3:
        return num > 1
    elif num % 6 != 1 and num % 6 != 5:
        return False
    sqrt_num = math.floor(math.sqrt(num) + 1)
    for i in range(5, sqrt_num, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


n = int(input())

count = 0
minuend = -1
subtrahend = -1
if n < 11:
    for i in range(n + 1):
        if isPrime(i):
            minuend = i
            if minuend - subtrahend == 2:
                count += 1
            subtrahend = i
elif n >= 11:
    count += 2
    for i in range(11, n + 1, 2):
        if isPrime(i):
            minuend = i
            if minuend - subtrahend == 2:
                count += 1
            subtrahend = i

print(count)
