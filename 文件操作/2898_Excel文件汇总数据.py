import openpyxl

wb = openpyxl.load_workbook('D:\Code\Python\PyCharm\PyClass\素材\Excel\每个人的爱好.xlsx')
sheet = wb.active

hobbies = sheet['B1:H7']
cells = sheet['B2:H7']
sheet['I1'] = '所有爱好'
col = 2
for col_cells in cells:
    favorite = []
    for i in range(len(col_cells)):
        if col_cells[i].value == "是":
            favorite.append(hobbies[0][i].value)
    sheet['I'+str(col)] = ','.join(favorite)
    col += 1
    # print(favorite)
wb.save("爱好汇总.xlsx")


