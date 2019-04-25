#!/anaconda3/bin/python
# @Time    : 2019-04-21 18:59
# @Author  : zhou
# @File    : gridInpanel
# @Software: PyCharm
# @Description:

import wx
import wx.grid as gridlib


class TestTable(wx.grid.PyGridTableBase):

    def __init__(self):
        gridlib.GridTableBase.__init__(self)
        self.rowLabels = ["uno", "dos", "tres", "quatro", "cinco"]
        self.colLabels = ["学号", "姓名", "性别", "数学", "英语", "计算机"]

    def GetNumberRows(self):
        return 5

    def GetNumberCols(self):
        return 5

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return "(%s,%s)" % (self.rowLabels[row], self.colLabels[col])

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return self.rowLabels[row]


class CustTableGrid(gridlib.Grid):
    def __init__(self, parent):
        gridlib.Grid.__init__(self, parent, -1)

        table = TestTable()

        # The second parameter means that the grid is to take ownership of the
        # table and will destroy it when done.  Otherwise you would need to keep
        # a reference to it and call it's Destroy method later.
        self.SetTable(table, True)

        # self.SetRowLabelSize(0)
        self.SetMargins(0, 0)
        self.AutoSizeColumns(False)


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Grid Table",
                          size=(400, 400))
        panel1 = wx.Panel(self, -1)
        panel2 = wx.Panel(self, -1)
        panel3 = wx.Panel(self, -1)
        hbox1 = wx.BoxSizer(wx.VERTICAL)

        hbox1.Add(panel1, 1, wx.EXPAND | wx.ALL, 10)
        hbox1.Add(panel2, 1, wx.EXPAND | wx.ALL, 10)
        hbox1.Add(panel3, 1, wx.EXPAND | wx.ALL, 10)

        table = CustTableGrid(panel2)
        tblSizer = wx.BoxSizer(wx.VERTICAL)
        tblSizer.Add(table, 1, wx.ALL | wx.EXPAND, 5)
        panel2.SetSizer(tblSizer)

        self.SetSizer(hbox1)


app = wx.App()
frame = TestFrame()
frame.Show()
app.MainLoop()
