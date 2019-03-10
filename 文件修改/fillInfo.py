#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-10 01:14
# @Author  : zhou
# @File    : fillInfo
# @Software: PyCharm
# @Description: 填写python PAT实验报告中个人信息

import docx
from docx.opc import exceptions
import os

className = input('请输入班级：')
name = input('请输入姓名：')
num = input('请输入学号：')
read_file_dirs = input('请输入要填写信息的文件所在文件夹路径,若有多个文件夹以空格隔开：').split(' ')
# filename = input()
for read_file_dir in read_file_dirs:
    if os.path.exists(read_file_dir) and os.path.isdir(read_file_dir):
        print(read_file_dir + ":")
        filenames = os.listdir(read_file_dir)
        os.chdir(read_file_dir)
        for filename in filenames:
            portion = os.path.splitext(filename)
            print(filename, end='：')
            if portion[1] == '.docx':
                try:
                    doc = docx.Document(filename)
                    table = doc.tables[0]
                    cell = table.rows[1].cells
                    cell[1].text = className
                    cell[3].text = name
                    cell[5].text = num
                    doc.save(filename)
                    print("修改成功")
                except exceptions.PackageNotFoundError as e:
                    print("文件打开失败", e)
                except Exception as e:
                    print(e)
            else:
                print('文件格式错误')
        os.chdir('..')
