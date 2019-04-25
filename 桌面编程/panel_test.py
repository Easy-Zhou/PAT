#!/anaconda3/bin/python
# @Time    : 2019-04-21 18:59
# @Author  : zhou
# @File    : gridInpanel
# @Software: PyCharm
# @Description:

import wx
import wx.grid as gridlib

import pymysql
import configparser


class Database:
    """ 数据库处理类 """

    def __init__(self, con_filename):
        config = configparser.ConfigParser()
        config.read(con_filename)
        host = config['db']['host']
        port = config.getint('db', 'port')
        user = config['db']['user']
        password = config['db']['password']
        database = config['db']['database']
        charset = config['db']['charset']

        self.__connect = pymysql.connect(host=host, port=port, user=user,
                                         password=password, database=database, charset=charset)

        self.__cursor = self.__connect.cursor()

    def query(self, sql):
        sql = sql
        self.__cursor.execute(sql)
        return self.__cursor.fetchone()

    def query_all(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def insert_one(self, sql):
        sql = sql
        result = self.__cursor.execute(sql)
        return result

    def insert_many(self, sql, data):
        result = self.__cursor.executemany(sql, data)
        return result

    def delete_one(self, sql):
        result = self.__cursor.execute(sql)
        return result

    def delete_many(self, sql, data):
        result = self.__cursor.executemany(sql, data)
        return result

    def __del__(self):
        self.__cursor.close()
        self.__connect.close()


class TestTable(wx.grid.PyGridTableBase):

    def __init__(self):
        gridlib.GridTableBase.__init__(self)
        sql = "select count(*) from student"
        self.db = Database('../数据库编程/configure.ini')

        self.rowLength = self.db.query(sql)[0]
        # self.rowLabels = ["uno", "dos", "tres", "quatro", "cinco"]
        self.colLabels = ["学号", "姓名", "性别", "数学", "英语", "计算机"]

    def GetNumberRows(self):
        return self.rowLength

    def GetNumberCols(self):
        return 6

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        sql = "select * from student"
        return self.db.query_all(sql)[row][col]

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        # return self.rowLabels[row]
        return "%d" % [i for i in range(1, self.rowLength + 1)][row]

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

        for i in range(table.rowLength):
            for j in range(6):
                self.SetCellAlignment(i, j, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        for i in range(6):
            self.SetColSize(i, 80)


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Grid Table",
                          size=(400, 400))

        self.icon = wx.Icon('icon/dog4.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.s = "准备就绪"
        self.statusBar = wx.StatusBar(self, -1)
        self.statusBar.SetFieldsCount(1)
        self.statusBar.SetStatusText(self.s)
        self.SetStatusBar(self.statusBar)

        panel1 = wx.Panel(self, -1)
        panel2 = wx.Panel(self, -1)
        panel3 = wx.Panel(self, -1)
        hbox1 = wx.BoxSizer(wx.VERTICAL)

        hbox1.Add(panel1, 1, wx.EXPAND | wx.ALL, 10)
        hbox1.Add(panel2, 1, wx.EXPAND | wx.ALL, 10)
        hbox1.Add(panel3, 0, wx.EXPAND | wx.ALL, 10)

        table = CustTableGrid(panel2)
        tblSizer = wx.BoxSizer(wx.VERTICAL)
        tblSizer.Add(table, 1, wx.ALL, 5)
        panel2.SetSizer(tblSizer)
        text = wx.StaticText(panel3,-1,"stests")
        self.SetSizer(hbox1)


app = wx.App()
frame = TestFrame()
frame.Show()
app.MainLoop()
