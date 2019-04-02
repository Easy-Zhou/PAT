#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-27 08:15
# @Author  : zhou
# @File    : 1054 求平均值
# @Software: PyCharm
# @Description: 
import math



def isLegal(st):
    try:
        float(st)
        if '.' in st and len(st.split('.')[-1]) > 2:
            raise Exception
        elif -1000 <= float(st) <= 1000:
            ave_list.append(float(st))
        else:
            raise Exception('ttt')
    except Exception as e:
        print('ERROR: %s is not a legal number' % st)


n = int(input())

str_in = input().split()
ave_list = []
for i in str_in:
    isLegal(i)
if len(ave_list) == 0:
    print('The average of 0 numbers is Undefined')

elif len(ave_list) == 1:
    print('The average of %d number is %.2f' % (len(ave_list), round(sum(ave_list) / len(ave_list) + 0.001, 2)))
else:
    print('The average of %d numbers is %.2f' % (len(ave_list), sum(ave_list) / len(ave_list)))
