#!/anaconda3/bin/python
# @Time    : 2019-04-26 13:14
# @Author  : zhou
# @File    : 框架
# @Software: PyCharm
# @Description: 

import time
import threading


def thread_body():
    t = threading.current_thread()  # 获取当前线程对象
    for n in range(5):
        # 当前线程名
        print('第{0}次执行线程{1}'.format(n, t.name))
        # 线程休眠
        time.sleep(1)
    print('线程{0}执行完成！'.format(t.name))


t1 = threading.Thread(target=thread_body)
t1.start()
t2 = threading.Thread(target=thread_body, name='MyThread')
t2.start()
