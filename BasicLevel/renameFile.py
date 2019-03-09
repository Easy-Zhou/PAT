#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-10 00:32
# @Author  : zhou
# @File    : renameFile
# @Software: PyCharm
# @Description: 

import os

num = input('请输入学号：')
name = input('请输入姓名：')
print(os.getcwd())
read_file_dirs = input('请输入要修改文件扩展名的路径,若有多个文件夹以空格隔开：').split(' ')

for read_file_dir in read_file_dirs:
    if os.path.exists(read_file_dir) and os.path.isdir(read_file_dir):
        files = os.listdir(read_file_dir)  # 列出当前目录下所有的文件
        for filename in files:

            name_l = filename.split('-')
            if len(name_l) == 4:
                newName = name_l[0] + '-' + num + '-' + name + '-' + name_l[3]
                os.chdir(read_file_dir)
                os.rename(filename, newName)
                print(os.path.basename(filename) + ' -> ' + os.path.basename(newName))
            else:
                print('not the aim file')
        os.chdir('..')
    else:
        print(read_file_dir,"路径不存在或不是一个目录")

    # portion = os.path.splitext(filename) # 分离文件名字和后缀
    # if portion[1] ==ext_from:  #检测扩展名
    #     newname = portion[0]+ext_to  #改新的新扩展名
    #     os.chdir(read_file_dir)
    #     os.rename(filename,newname)
