#!/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-25 22:56
# @Author  : zhou
# @File    : 1044 火星数字
# @Software: PyCharm
# @Description: 

n = int(input())

low = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
high = ['tret', 'tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']


def num_to_word(str_num):
    """

    :return: None
    """
    out_list = []
    num = int(str_num)
    while True:
        if num % 13 == 0 and num != 0:
            out_list.append(high[num//13])
            break
        out_list.append(low[num % 13])
        num = num // 13
        if num == 0:
            break
        out_list.append(high[num])
        break
    print(' '.join(out_list[::-1]))


def word_to_num(str):
    """

    :param str:
    :return:
    """
    str_list = str.split()
    if len(str_list) == 1 and str_list[0] in low:
        print(low.index(str_list[0]))
    elif len(str_list) == 1 and str_list[0] not in low:
        print(high.index(str_list[0])*13)
    elif len(str_list) == 2:
        print(low.index(str_list[1]) + high.index(str_list[0]) * 13)


for i in range(n):
    str_in = input()
    if str_in.isdigit():
        num_to_word(str_in)
    else:
        word_to_num(str_in)
