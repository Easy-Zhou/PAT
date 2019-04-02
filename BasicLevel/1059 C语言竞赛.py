#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-28 15:24
# @Author  : zhou
# @File    : 1059 C语言竞赛
# @Software: PyCharm
# @Description: 

import math


def isPrime(num):
    """
    :param num
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
rank = dict()
checked_set = set()
count = 1
for i in range(n):
    rank[input()] = count
    count += 1

m = int(input())
for k in range(m):
    Id = input()
    Info = ''
    if Id in checked_set:
        Info = 'Checked'
    elif Id not in rank.keys():
        Info = 'Are you kidding?'
    elif rank[Id] == 1:
        Info = 'Mystery Award'
        checked_set.add(Id)
    elif isPrime(rank[Id]):
        Info = 'Minion'
        checked_set.add(Id)
    else:
        Info = 'Chocolate'
        checked_set.add(Id)
    print('%s: %s' % (Id, Info))
