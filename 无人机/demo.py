#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-08 14:53
# @Author  : zhou
# @File    : demo
# @Software: PyCharm
# @Description: 

import socket
import time

secs = 5  # 秒数


address = ('192.168.10.1', 8889)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print("请输入你的操控命令!，按回车退出本程序，但也失去对飞机的控制，建议让飞机做落后再退出")


while True:
    msg = input("请输入你的操控命令: ")
    msg = msg.encode(encoding='utf-8')
    if not msg:
        break
    s.sendto(msg,address)
    print(s.recv(1024).decode('utf-8'))
s.close()

time.time()
# sec=5
# msg=msg1.encode(encoding='utf-8')
# s.sendto(msg, address)
# time.sleep(sec)
# pass
# msg=msg2.encode(encoding='utf-8')
# s.sendto(msg, address)
# time.sleep(sec)
# pass
# msg=msg3.encode(encoding='utf-8')
# s.sendto(msg, address)
# time.sleep(sec)
# pass
# msg=msg4.encode(encoding='utf-8')
# s.sendto(msg, address)
# time.sleep(sec)
# pass
# msg=msg5.encode(encoding='utf-8')
# s.sendto(msg, address)
# time.sleep(sec)
# pass
# msg=msg6.encode(encoding='utf-8')
# s.sendto(msg, address)
# time.sleep(sec)
# pass
# msg=msg7.encode(encoding='utf-8')
# s.sendto(msg, address)
# s.close()
