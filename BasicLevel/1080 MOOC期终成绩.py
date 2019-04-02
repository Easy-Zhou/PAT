#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-30 15:27
# @Author  : zhou
# @File    : 1080 MOOC期终成绩
# @Software: PyCharm
# @Description: 

l_n = list(map(int, input().split()))
P = dict()
M = dict()
N = dict()
result = []
for i in range(l_n[0]):
    temp_in = input().split()
    P[temp_in[0]] = int(temp_in[1])

for i in range(l_n[1]):
    temp_in = input().split()
    M[temp_in[0]] = int(temp_in[1])

for i in range(l_n[2]):
    temp_in = input().split()
    N[temp_in[0]] = int(temp_in[1])

for k, v in P.items():
    G = 0
    n = N.get(k)
    m = M.get(k)
    if n is None or v < 200:
        pass
    else:
        if m is not None:
            if m > n:
                G = round(0.4 * m + 0.6 * n)
            else:
                G = n
            if G >= 60:
                result.append([k, v, m, n, G])

        elif n >= 60:
            result.append([k, v, -1, n, n])

result = sorted(result, key=lambda x: (-x[4], x[0]))
for i in result:
    print(i[0], i[1], i[2], i[3], i[4])
