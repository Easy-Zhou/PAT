#!/anaconda3/bin/python
# @Time    : 2019-04-26 14:22
# @Author  : zhou
# @File    : 1793-输出HelloWorld二
# @Software: PyCharm
# @Description: 

import time
import threading


def thread_body():
    for i in range(10):
        # 当前线程名
        print("HelloWorld")
        # 线程休眠
        time.sleep(1)


t1 = threading.Thread(target=thread_body)
t1.start()

