#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-24 22:19
# @Author  : zhou
# @File    : 1013 数素数
# @Software: PyCharm
# @Description:
import math

n, m = map(int, input().split())


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


Prime = [2, 3, 5, 7]
count = 4
i = 11

while True:
    if count > m:
        break
    if isPrime(i):
        Prime.append(i)
        count += 1
    if isPrime(i + 2):
        Prime.append(i + 2)
        count += 1
    i += 6

end_count = 1
for i in range(n - 1, m):
    if end_count % 10 == 0 or i == m -1:
        print(Prime[i])
    else:
        print(Prime[i], end=' ')
    end_count += 1
