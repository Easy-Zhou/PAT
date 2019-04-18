#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-11 15:51
# @Author  : zhou
# @File    : receiveStatus
# @Software: PyCharm
# @Description: 

import socket
import sys

# 创建 socket 对象
serverSocket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM)

# 获取本地主机名
host = socket.gethostname()

port = 8890

# 绑定端口号
serverSocket.bind((host, port))

# 设置最大连接数，超过后排队
serverSocket.listen(5)

while True:
    # 建立客户端连接
    clientSocket, addr = serverSocket.accept()

    print("连接地址: %s" % str(addr))

    msg = 'yy！' + "\r\n"
    print(clientSocket.recv(1024).decode('utf-8'))
    clientSocket.close()