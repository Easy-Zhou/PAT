import docx
import os

className = '16计算机1'
name = "周易"
num = '16211160127'
# filename = input()
doc = docx.Document('tres.docx')
for table in doc.tables:
    cell = table.rows[1].cells
    cell[1].text = className
    cell[3].text = name
    cell[5].text = num
doc.save('tres.docx')
