#!/anaconda3/bin/python
# @Time    : 2019-04-02 21:32
# @Author  : zhou
# @File    : 1092 最好吃的月饼
# @Software: PyCharm
# @Description: 

import numpy as np

N, M = map(int, input().split())

result = np.zeros(N)

for i in range(M):
    result += np.array(list(map(int, input().split())))

a = np.max(result)
print('%d' % a)
index = np.where(result == a)
for i in index[0][:-1]:
    print(i + 1, end=' ')
print(index[0][-1] + 1)
