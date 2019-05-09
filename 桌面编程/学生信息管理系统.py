#!/anaconda3/bin/python
# @Time    : 2019-04-21 18:47
# @Author  : zhou
# @File    : 学生信息管理系统
# @Software: PyCharm
# @Description: 


import wx
import wx.grid as gridlib
import wx.grid

import pymysql
import configparser


class Database:
    """ 数据库处理类 """

    def __init__(self, con_filename='configure.ini'):
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
        self.__connect.commit()
        return result

    def insert_many(self, sql, data):
        result = self.__cursor.executemany(sql, data)
        self.__connect.commit()
        return result

    def update(self, sql):
        result = self.__cursor.execute(sql)
        self.__connect.commit()
        return result

    def delete_one(self, sql):
        result = self.__cursor.execute(sql)
        self.__connect.commit()
        return result

    def delete_many(self, sql, data):
        result = self.__cursor.executemany(sql, data)
        self.__connect.commit()
        return result

    def __del__(self):
        self.__cursor.close()
        self.__connect.close()


class TestTable(wx.grid.GridTableBase):

    def __init__(self, condition):
        gridlib.GridTableBase.__init__(self)
        # self.rowLabels = ["uno", "dos", "tres", "quatro", "cinco"]
        self.condition = condition
        if self.condition == "":
            self.where = "1"
        else:
            self.where = "name like '%" + self.condition + "%'"
        sql = "select count(*) from student where " + self.where
        self.db = Database()

        self.rowLength = self.db.query(sql)[0]
        self.colLabels = ["学号", "姓名", "性别", "数学", "英语", "计算机"]

    def GetNumberRows(self):
        return self.rowLength

    def GetNumberCols(self):
        return 6

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        # return "(%s,%s)" % (self.rowLabels[row], self.colLabels[col])
        sql = "select * from student where " + self.where
        return self.db.query_all(sql)[row][col]

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return "%d" % [i for i in range(1, self.rowLength + 1)][row]


class CustTableGrid(gridlib.Grid):
    def __init__(self, parent, condition):
        gridlib.Grid.__init__(self, parent, -1)
        table = TestTable(condition)

        # The second parameter means that the grid is to take ownership of the
        # table and will destroy it when done.  Otherwise you would need to keep
        # a reference to it and call it's Destroy method later.
        self.SetTable(table, True)

        # self.SetRowLabelSize(0)
        self.SetMargins(0, 0)
        # self.AutoSizeColumns(False)
        self.AutoSizeColumns(False)
        for i in range(table.rowLength):
            for j in range(6):
                self.SetCellAlignment(i, j, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        for i in range(6):
            self.SetColSize(i, 80)


class NewFrame(wx.Frame):
    def __init__(self, title, parentFrame=None, data=None):
        wx.Frame.__init__(self, None, title=title, size=(280, 400))
        self.Center()
        self.parentFrame = parentFrame

        self.icon = wx.Icon('icon/dog4.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        panel = wx.Panel(self)
        vbox_whole = wx.BoxSizer(wx.VERTICAL)
        vbox_whole.Add(panel, 0, wx.ALL | wx.EXPAND | wx.CENTER, 10)

        st_num = wx.StaticText(panel, label="学号：")
        st_name = wx.StaticText(panel, label="姓名：")
        st_sex = wx.StaticText(panel, label="性别：")
        st_math = wx.StaticText(panel, label="数学：")
        st_english = wx.StaticText(panel, label="英语：")
        st_computer = wx.StaticText(panel, label="计算机：")
        self.tc_num = wx.TextCtrl(panel)
        self.tc_name = wx.TextCtrl(panel)
        self.tc_sex = wx.TextCtrl(panel)
        self.tc_math = wx.TextCtrl(panel)
        self.tc_english = wx.TextCtrl(panel)
        self.tc_computer = wx.TextCtrl(panel)

        if data is not None:
            self.tc_num.SetValue(data[0])
            self.tc_name.SetValue(data[1])
            self.tc_sex.SetValue(data[2])
            self.tc_math.SetValue(str(data[3]))
            self.tc_english.SetValue(str(data[4]))
            self.tc_computer.SetValue(str(data[5]))

        bt_ok = wx.Button(panel, 111, title)
        bt_cancel = wx.Button(panel, 112, "取消")

        self.Bind(wx.EVT_BUTTON, self.on_click, id=111)
        self.Bind(wx.EVT_BUTTON, self.on_click, id=112)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox_num = wx.BoxSizer(wx.HORIZONTAL)
        hbox_num.AddMany([st_num, self.tc_num])

        hbox_name = wx.BoxSizer(wx.HORIZONTAL)
        hbox_name.AddMany([st_name, self.tc_name])

        hbox_sex = wx.BoxSizer(wx.HORIZONTAL)
        hbox_sex.AddMany([st_sex, self.tc_sex])

        hbox_math = wx.BoxSizer(wx.HORIZONTAL)
        hbox_math.AddMany([st_math, self.tc_math])

        hbox_english = wx.BoxSizer(wx.HORIZONTAL)
        hbox_english.AddMany([st_english, self.tc_english])

        hbox_computer = wx.BoxSizer(wx.HORIZONTAL)
        hbox_computer.AddMany([st_computer, self.tc_computer])

        hbox_bt = wx.BoxSizer(wx.HORIZONTAL)
        hbox_bt.AddMany([(bt_ok, 1, wx.RIGHT, 10), (bt_cancel)])

        # bt_add = wx.Button(panel_bot, 102, "添加")
        # self.Bind(wx.EVT_BUTTON, self.on_click, id=102, )
        # bt_upt = wx.Button(panel_bot, 103, "修改")
        # bt_del = wx.Button(panel_bot, 104, "删除")
        # hbox_bot.AddMany([(bt_add, 1, wx.LEFT, 5), (bt_upt, 1, wx.LEFT, 5),
        #                   (bt_del, 1, wx.LEFT | wx.RIGHT, 5)])

        vbox.AddMany([(hbox_num, 1, wx.CENTER | wx.TOP, 20), (hbox_name, 1, wx.CENTER | wx.TOP, 20),
                      (hbox_sex, 1, wx.CENTER | wx.TOP, 20), (hbox_math, 1, wx.CENTER | wx.TOP, 20),
                      (hbox_english, 1, wx.CENTER | wx.TOP, 20), (hbox_computer, 1, wx.CENTER | wx.TOP, 20),
                      (hbox_bt, 1, wx.CENTER | wx.TOP | wx.BOTTOM, 30)])

        panel.SetSizer(vbox)
        self.SetSizer(vbox_whole)

    def on_click(self, event):
        eventId = event.GetId()
        if eventId == 111 and self.Title == "增加":
            self.parentFrame.Close(True)

            num = self.tc_num.GetValue()
            name = self.tc_name.GetValue()
            sex = self.tc_sex.GetValue()
            math = self.tc_math.GetValue()
            english = self.tc_english.GetValue()
            computer = self.tc_computer.GetValue()
            db = Database("configure.ini")
            sql = "insert into student values('%s','%s','%s',%s,%s,%s)" % (num, name, sex, math, english, computer)
            db.insert_one(sql)

            new_frame = MyFrame(message=(self.Title + "成功!"))
            new_frame.Show()
            self.Close(True)

        elif eventId == 111 and self.Title == "修改":
            self.parentFrame.Close(True)

            num = self.tc_num.GetValue()
            name = self.tc_name.GetValue()
            sex = self.tc_sex.GetValue()
            math = self.tc_math.GetValue()
            english = self.tc_english.GetValue()
            computer = self.tc_computer.GetValue()
            db = Database()
            # sql = "update student set name=" + name + ",sex=" + sex + ",math=" + math + \
            #       ",english=" + english + ",computer=" + computer + " where number=" + num
            sql = "update student set name='%s', sex='%s', math=%s, english=%s, computer=%s where number='%s'" \
                  % (name, sex, math, english, computer, num)
            db.update(sql)
            new_frame = MyFrame(message=(self.Title + "成功！"))
            new_frame.Show()
            self.Close(True)

        elif eventId == 112:
            self.Close(True)


class MyFrame(wx.Frame):
    def __init__(self, condition="", message="准备就绪"):
        wx.Frame.__init__(self, None, title="学生信息管理系统",
                          size=(595, 400))

        self.Center()
        self.tbSelectedId = ""
        self.icon = wx.Icon('icon/dog4.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        if condition == "":
            self.s = message
        else:
            self.s = message
        self.statusBar = wx.StatusBar(self, -1)
        self.statusBar.SetFieldsCount(1)
        self.statusBar.SetStatusText(self.s)
        self.SetStatusBar(self.statusBar)

        # 定义3个底层Panel并添加绑定在同一个BoxSizer中
        panel_top = wx.Panel(self, -1)
        self.panel_mid = wx.Panel(self, -1)
        panel_bot = wx.Panel(self, -1)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(panel_top, 0, wx.EXPAND | wx.TOP | wx.Left | wx.RIGHT, 10)
        vbox1.Add(self.panel_mid, 1, wx.EXPAND | wx.TOP | wx.Left | wx.RIGHT, 10)
        vbox1.Add(panel_bot, 0, wx.EXPAND | wx.ALL, 10)

        # 添加上半部份查询相关控件
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel_top, -1, "请输入名字:")
        self.tc = wx.TextCtrl(panel_top)
        self.tc.SetValue(condition)
        bt_que = wx.Button(panel_top, 101, "查询")
        self.Bind(wx.EVT_BUTTON, self.on_click, id=101, )
        hbox1.AddMany([(st1, 1, wx.ALL | wx.ALIGN_RIGHT, 5), (self.tc, 1, wx.ALL),
                       (bt_que, 1, wx.LEFT | wx.RIGHT, 5)])
        vbox_top = wx.BoxSizer(wx.VERTICAL)
        vbox_top.Add(hbox1, 1, wx.CENTER | wx.ALL, 0)
        panel_top.SetSizer(vbox_top)

        # 设置表格的BoxSizer
        self.table = CustTableGrid(self.panel_mid, condition)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.select_row)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.select_row)
        self.tblSizer = wx.BoxSizer(wx.VERTICAL)
        self.tblSizer.Add(self.table, 1, wx.ALL | wx.EXPAND, 0)
        self.panel_mid.SetSizer(self.tblSizer)

        # 设置底部按钮的布局
        hbox_bot = wx.BoxSizer(wx.HORIZONTAL)
        bt_add = wx.Button(panel_bot, 102, "添加")
        self.Bind(wx.EVT_BUTTON, self.on_click, id=102)
        bt_upt = wx.Button(panel_bot, 103, "修改")
        self.Bind(wx.EVT_BUTTON, self.on_click, id=103)
        bt_del = wx.Button(panel_bot, 104, "删除")
        self.Bind(wx.EVT_BUTTON, self.on_click, id=104)
        hbox_bot.AddMany([(bt_add, 1, wx.LEFT, 5), (bt_upt, 1, wx.LEFT, 5),
                          (bt_del, 1, wx.LEFT | wx.RIGHT, 5)])
        vbox_bot = wx.BoxSizer(wx.VERTICAL)
        vbox_bot.Add(hbox_bot, 1, wx.CENTER | wx.ALL, 0)
        panel_bot.SetSizer(vbox_bot)

        self.SetSizer(vbox1)

    def on_click(self, event):
        """
        """
        event_id = event.GetId()
        if event_id == 101:  # 查询

            condition = self.tc.GetValue()
            new_frame = MyFrame(condition, "查询成功！")
            new_frame.Show()
            self.Close(True)
            # self.statusBar.SetStatusText(self.s)
        elif event_id == 102:  # 增加
            self.set_status_bar("增加操作")
            add_frame = NewFrame('增加', self)
            add_frame.Show()

        elif event_id == 103:  # 修改
            self.set_status_bar("修改操作")
            db = Database()
            data = db.query("select * from student where number=" + self.tbSelectedId)
            update_frame = NewFrame('修改', self, data)
            update_frame.Show()

        elif event_id == 104:  # 删除
            self.set_status_bar("删除操作")
            db = Database()
            db.delete_one("delete from student where number=" + self.tbSelectedId)
            new_frame = MyFrame(message="删除成功！")
            new_frame.Show()
            self.Close(True)

    def set_status_bar(self, message):
        self.s = message
        self.statusBar.SetStatusText(self.s)

    def select_row(self, event):
        row_selected = event.GetRow()

        self.s = str(row_selected)
        self.tbSelectedId = self.table.GetCellValue(row_selected, 0)
        self.statusBar.SetStatusText("选中第" + str(row_selected + 1) + "行")


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0


if __name__ == "__main__":
    app = App()
    app.MainLoop()
