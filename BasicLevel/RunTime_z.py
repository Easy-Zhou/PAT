#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 08:29
# @Author  : zhou
# @File    : RunTime_z
# @Software: PyCharm
# @Description: 

import time


def Time(func):
    """
    用于计算函数运行时间的装饰器
    :param func:
    :return:
    """

    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("运行时间：", end_time - start_time)

    return deco


if __name__ == '__main__':
    pass