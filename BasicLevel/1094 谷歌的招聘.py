#!/anaconda3/bin/python
# @Time    : 2019-04-02 22:16
# @Author  : zhou
# @File    : 1094 谷歌的招聘
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


t, n = map(int, input().split())
str_in = input()

for i in range(t-n+1):
    temp = str_in[i:i+n]
    if isPrime(int(temp)):
        print(temp)
        break
else:
    print(404)


