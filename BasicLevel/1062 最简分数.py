#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-28 16:03
# @Author  : zhou
# @File    : 1062 最简分数
# @Software: PyCharm
# @Description: 

import math

str_in = input().split()
a = min(eval(str_in[0]), eval(str_in[1]))
b = max(eval(str_in[0]), eval(str_in[1]))
down = int(str_in[2])

start = math.floor(a * down)
end = math.ceil(b * down)


def is_co_prime(i, down):
    while True:
        if i == 0:
            break
        i, down = down % i, i

    if down == 1:
        return True
    else:
        return False


result = []
for i in range(start, end):
    if is_co_prime(i, down) and a < i / down < b:
        result.append("%d/%d" % (i, down))

print(' '.join(result))
