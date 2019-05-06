#!/anaconda3/bin/python
# @Time    : 2019-04-26 17:21
# @Author  : zhou
# @File    : 2897_线程通信
# @Software: PyCharm
# @Description: 

import time
import threading

class Stack:

    def __init__(self):
        self.pointer = -1
        self.data = [-1] * 5

    def push(self,x):
        global event
        while self.pointer == len(self.data) -1:
            event.wait()
        event.set()
        self.pointer += 1
        self.data[self.pointer] = x

    def pop(self):
        global event
        while self.pointer == -1:
            event.wait()
        event.set()
        self.pointer -= 1
        return self.data[self.pointer +1]


def product():
    global stack
    for i in range(10):
        stack.push(i)
        print("生产{0}".format(i))
        time.sleep(1)


def customer():
    global stack
    for i in range(10):
        result = stack.pop()
        print("消费{0}".format(result))
        time.sleep(1)


stack = Stack()
event = threading.Event()
product = threading.Thread(target=product)
customer = threading.Thread(target=customer)

product.start()
customer.start()
