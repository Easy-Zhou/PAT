#!/anaconda3/bin/python
# @Time    : 2019-05-10 15:29
# @Author  : zhou
# @File    : 2904-随机生成成绩并处理
# @Software: PyCharm
# @Description: 

import openpyxl
import random

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = '姓名'
sheet['B1'] = '课程'
sheet['C1'] = '成绩'
for i in range(2, 1300):
    x = random.choice('赵钱孙李')
    y = random.choice('伟昀琛东')
    z = random.choice('坤艳志 ')
    name = x + y + z
    course = random.choice(['语文', '数学', '英语'])
    grade = random.randrange(0, 101)
    A = 'A' + str(i)
    B = 'B' + str(i)
    C = 'C' + str(i)
    sheet[A] = name
    sheet[B] = course
    sheet[C] = grade
wb.save('test.xlsx')


newRows = []

for row in sheet.rows:
    flag = 0
    for item in newRows:
        if row[0].value == item[0] and row[1].value == item[1] and float(row[2].value) > float(item[2]):
            # newRows.append([row[0].value,row[1].value,row[2].value])
            item[2] = row[2].value
            flag = 1
            break
        elif row[0].value == item[0] and row[1].value == item[1]:
            flag = 1
    if flag == 0:
        newRows.append([row[0].value, row[1].value, row[2].value])

wb_result = openpyxl.Workbook()
sheet_result = wb_result.active

for row in newRows:
    sheet_result.append(row)

wb_result.save('result.xlsx')


