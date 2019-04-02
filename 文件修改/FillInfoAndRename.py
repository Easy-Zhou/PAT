#!/anaconda3/bin/python
# @Time    : 2019-04-02 23:38
# @Author  : zhou
# @File    : fillInfoAndRename
# @Software: PyCharm
# @Description: 填写实验报告模板表格中的个人信息以及文件名

import docx
from docx.opc import exceptions
from docx.shared import Pt
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
                    doc.styles['Normal'].font.name = '微软雅黑'
                    doc.styles['Normal'].font.size = Pt(8)
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
            name_l = filename.split('-')
            if len(name_l) == 4:
                newName = name_l[0] + '-' + num + '-' + name + '-' + name_l[3]
                os.rename(filename, newName)
                print(os.path.basename(filename) + ' -> ' + os.path.basename(newName))
            else:
                print('not the aim file')
        os.chdir('..')
    else:
        print(read_file_dir,"路径不存在或不是一个目录")