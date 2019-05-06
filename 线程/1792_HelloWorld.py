#!/anaconda3/bin/python
# @Time    : 2019-04-26 13:28
# @Author  : zhou
# @File    : 1792_HelloWorld
# @Software: PyCharm
# @Description:

import time
import threading


def thread_body():
    t = threading.current_thread()  # 获取当前线程对象
    while True:
        # 当前线程名
        print("HelloWorld")
        # 线程休眠
        time.sleep(1)


t1 = threading.Thread(target=thread_body)
t1.start()


