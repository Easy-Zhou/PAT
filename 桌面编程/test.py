#!/anaconda3/bin/python
# @Time    : 2019-04-21 21:17
# @Author  : zhou
# @File    : test
# @Software: PyCharm
# @Description: 


'''一个图书管理系统，能够实现增加书籍，删除书籍，
修改书籍和查看图书详情，基于mysql数据库和
wxPython'''

import wx
import pymysql

__metaclass__ = type

# author = liuwei  date = 2017-06-02
from datetime import *  # 导入日期模块

# __metaclass__ = type


class Book:
    '''一个书本信息类，包括书本名字，作者名字和书本简单信息'''

    def __init__(self, bookName="", author="", content=""):
        self.bookName = bookName  # 书本名字
        self.author = author  # 作者名字
        self.content = content  # 书本信息
        self.add_date = date.today()  # 书本添加日期

    def setBookName(self, name):
        self.bookName = name

    def getBookName(self):
        return self.bookName

    def setAuthor(self, author):
        self.author = author

    def getAuthor(self):
        return self.author

    def setContent(self, content):
        self.content = content

    def getContent(self):
        return self.content

    def getAddDate(self):
        return self.add_date


# if __name__ == "

###########databaseHelper类：

# import pymysql
# from book import *

# __metaclass__ = type


class DBHelper:
    def getCon(self):
        '''获取操作数据库的curcor即游标，首先的建立连接，需要服务器地址，端口号，用户名，密码和数据库名'''
        # 为了能用中文，得加上编码方式
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="zhou123", db="library",
                               charset="utf8")

        return conn

    def insertBook(self, book):
        '''向数据库中book表插入书本信息，book为Book类对象，包含书本基本信息'''
        sql = "insert into book(name, author, content, add_date) values(%s, %s, %s, %s)"

        conn = self.getCon();
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (book.getBookName(), book.getAuthor(), book.getContent(), book.getAddDate()))

        conn.commit()
        cursor.close()
        conn.close()

        new_id = cursor.lastrowid
        print("新插入键值id为:", new_id)

        return new_id

    def getAllBook(self):
        '''返回数据库中，book表中所有的书本信息'''
        sql = "select *from book"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        rownum = cursor.execute(sql)  # 执行并返回找到的行数

        # 获取查询结果
        rows = cursor.fetchall()
        list = []

        for item in rows:
            bitem = (item[0], item[1], str(item[4]))

            list.append(bitem)

        conn.commit()
        cursor.close()
        conn.close()

        return list

    def getBookById(self, bookid):
        '''根据书本id值来寻找书本信息'''

        sql = "select book.name, book.author, book.content from book  where id=%s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (bookid,))  # 参数以元组形式给出
        row = cursor.fetchone()  # 取到第一个结果

        conn.commit()
        cursor.close()
        conn.close()

        return row  # 返回该书本信息

    def saveUpdate(self, bookid, book):
        '''用book对象来修改id为bookid的书本信息'''
        sql = "update book set book.name=%s, book.author=%s, book.content=%s where book.id=%s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (book.getBookName(), book.getAuthor(), book.getContent(), bookid))

        conn.commit()
        cursor.close()
        conn.close()

    def deleteBook(self, bookid):
        '''根据书本id来删除书籍'''
        sql = "delete from book where book.id = %s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (bookid,))

        conn.commit()
        cursor.close()
        conn.close()


# if __name__ == '__main__':
#     db = DBHelper()
#     #book = Book("秦腔", "贾凹平", "讲的是大西北夏家和白家的事情，由引生口述。")
#     #db.insertBook(book)
#     list = db.getAllBook()
#     for item in list:
#         print(item)
#
# ---------------------
# 作者：玩人
# 来源：CSDN
# 原文：https://blog.csdn.net/jeryjeryjery/article/details/72852318
# 版权声明：本文为博主原创文章，转载请附上博文链接！

###########databaseHelper类：


class AddFrame(wx.Frame):
    '''添加书籍弹出的小窗口'''

    def __init__(self, parent, title):
        '''初始化该小窗口的布局'''

        self.mainframe = parent
        # 生成一个300*300的框
        wx.Frame.__init__(self, parent, title=title, size=(400, 250))

        self.panel = wx.Panel(self, pos=(0, 0), size=(400, 250))
        self.panel.SetBackgroundColour("#FFFFFF")  # 背景为白色

        # 三个编辑框，分别用来编辑书名，作者，书籍相关信息
        bookName_tip = wx.StaticText(self.panel, label="书名:", pos=(5, 8), size=(35, 25))
        bookName_tip.SetBackgroundColour("#FFFFFF")
        bookName_text = wx.TextCtrl(self.panel, pos=(40, 5), size=(340, 25))
        self.name = bookName_text

        author_tip = wx.StaticText(self.panel, label="作者:", pos=(5, 38), size=(35, 25))
        author_tip.SetBackgroundColour("#FFFFFF")
        author_text = wx.TextCtrl(self.panel, pos=(40, 35), size=(340, 25))
        self.author = author_text

        content_tip = wx.StaticText(self.panel, label="内容:", pos=(5, 68), size=(340, 25))
        content_tip.SetBackgroundColour("#FFFFFF")
        content_text = wx.TextCtrl(self.panel, pos=(40, 65), size=(340, 100), style=wx.TE_MULTILINE)
        self.content = content_text

        save_button = wx.Button(self.panel, label="保存书籍", pos=(160, 170))
        self.Bind(wx.EVT_BUTTON, self.saveBook, save_button)

        # 需要用到的数据库接口
        self.dbhelper = DBHelper()

    def saveBook(self, evt):
        '''第一步：获取text中文本；第二步，连接数据库；第三步插入并获得主键；第四步添加到ListCtrl中'''
        bookName = self.name.GetValue()
        author = self.author.GetValue()
        content = self.content.GetValue()

        print("书名:" + bookName)
        if bookName == "" or author == "" or content == "":
            print("进来了")
            warn = wx.MessageDialog(self, message="所有信息不能为空！！！", caption="错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            print("开始插入到数据库中")
            book = Book(bookName, author, content)
            book_id = self.dbhelper.insertBook(book)
            self.mainframe.addToList(book_id, book)

        self.Destroy()


class UpdateFrame(wx.Frame):
    def __init__(self, parent, title, select_id):
        '''初始化更新图书信息界面总布局'''

        wx.Frame(parent, title=title, size=(400, 250))

        # 用来调用父frame,便于更新
        self.mainframe = parent
        # 生成一个300*300的框
        wx.Frame.__init__(self, parent, title=title, size=(400, 250))

        self.panel = wx.Panel(self, pos=(0, 0), size=(400, 250))
        self.panel.SetBackgroundColour("#FFFFFF")  # 背景为白色

        # 三个编辑框，分别用来编辑书名，作者，书籍相关信息
        bookName_tip = wx.StaticText(self.panel, label="书名:", pos=(5, 8), size=(35, 25))
        bookName_tip.SetBackgroundColour("#FFFFFF")
        bookName_text = wx.TextCtrl(self.panel, pos=(40, 5), size=(340, 25))
        self.name = bookName_text

        author_tip = wx.StaticText(self.panel, label="作者:", pos=(5, 38), size=(35, 25))
        author_tip.SetBackgroundColour("#FFFFFF")
        author_text = wx.TextCtrl(self.panel, pos=(40, 35), size=(340, 25))
        self.author = author_text

        content_tip = wx.StaticText(self.panel, label="内容:", pos=(5, 68), size=(340, 25))
        content_tip.SetBackgroundColour("#FFFFFF")
        content_text = wx.TextCtrl(self.panel, pos=(40, 65), size=(340, 100), style=wx.TE_MULTILINE)
        self.content = content_text

        save_button = wx.Button(self.panel, label="保存修改", pos=(160, 170))
        self.Bind(wx.EVT_BUTTON, self.saveUpdate, save_button)

        # 选中的id和bookid
        self.select_id = select_id
        self.bookid = self.mainframe.list.GetItem(select_id, 0).Text  # 获取第select_id行的第0列的值
        print(select_id, self.bookid)
        # 需要用到的数据库接口
        self.dbhelper = DBHelper()
        self.showAllText()  # 展现所有的text原来取值

    def showAllText(self):
        '''显示概述本原始信息'''
        data = self.dbhelper.getBookById(self.bookid)  # 通过id获取书本信息

        self.name.SetValue(data[0])  # 设置值
        self.author.SetValue(data[1])
        self.content.SetValue(data[2])

    def saveUpdate(self, evt):
        '''保存修改后的值'''
        bookName = self.name.GetValue()  # 获得修改后的值
        author = self.author.GetValue()
        content = self.content.GetValue()

        print("书名:" + bookName)
        if bookName == "" or author == "" or content == "":
            print("进来了")
            warn = wx.MessageDialog(self, message="所有信息不能为空！！！", caption="错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            print("开始将修改后的数据保存到数据库中")
            book = Book(bookName, author, content)  # 将数据封装到book对象中
            self.dbhelper.saveUpdate(self.bookid, book)
            self.mainframe.list.SetItem(self.select_id, 1, bookName)

        self.Destroy()  # 修改完后自动销毁


class ShowFrame(wx.Frame):
    '''用来显示书籍的信息'''

    def __init__(self, parent, title, select_id):
        '''初始化该小窗口的布局'''

        # 便于调用父窗口
        self.mainframe = parent

        # 生成一个300*300的框
        wx.Frame.__init__(self, parent, title=title, size=(400, 250))

        self.panel = wx.Panel(self, pos=(0, 0), size=(400, 250))
        self.panel.SetBackgroundColour("#FFFFFF")  # 背景为白色

        # 三个编辑框，分别用来编辑书名，作者，书籍相关信息
        bookName_tip = wx.StaticText(self.panel, label="书名:", pos=(5, 8), size=(35, 25))
        bookName_tip.SetBackgroundColour("#FFFFFF")
        bookName_text = wx.TextCtrl(self.panel, pos=(40, 5), size=(340, 25))
        bookName_text.SetEditable(False)
        self.name = bookName_text

        author_tip = wx.StaticText(self.panel, label="作者:", pos=(5, 38), size=(35, 25))
        author_tip.SetBackgroundColour("#FFFFFF")
        author_text = wx.TextCtrl(self.panel, pos=(40, 35), size=(340, 25))
        author_text.SetEditable(False)
        self.author = author_text

        content_tip = wx.StaticText(self.panel, label="内容:", pos=(5, 68), size=(340, 25))
        content_tip.SetBackgroundColour("#FFFFFF")
        content_text = wx.TextCtrl(self.panel, pos=(40, 65), size=(340, 100), style=wx.TE_MULTILINE)
        content_text.SetEditable(False)
        self.content = content_text

        # 选中的id和bookid
        self.select_id = select_id
        self.bookid = self.mainframe.list.GetItem(select_id, 0).Text  # 获取第select_id行的第0列的值

        # 需要用到的数据库接口
        self.dbhelper = DBHelper()
        self.showAllText()  # 展现所有的text原来取值

    def showAllText(self):
        '''显示概述本原始信息'''
        data = self.dbhelper.getBookById(self.bookid)  # 通过id获取书本信息

        self.name.SetValue(data[0])  # 设置值
        self.author.SetValue(data[1])
        self.content.SetValue(data[2])


class LibraryFrame(wx.Frame):
    def __init__(self, parent, title):
        '''初始化系统总体布局，包括各种控件'''

        # 生成一个宽为400，高为400的frame框
        wx.Frame.__init__(self, parent, title=title, size=(400, 400))

        # 定一个网格布局,两行一列
        self.main_layout = wx.BoxSizer(wx.VERTICAL)

        # 生成一个列表
        self.list = wx.ListCtrl(self, -1, size=(400, 300),
                                style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)  # | wx.LC_SINGLE_SEL
        # 列表有散列，分别是书本ID,书名，添加日期
        self.list.InsertColumn(0, "ID")
        self.list.InsertColumn(1, "书名")
        self.list.InsertColumn(2, "添加日期")
        # 设置各列的宽度
        self.list.SetColumnWidth(0, 60)  # 设置每一列的宽度
        self.list.SetColumnWidth(1, 230)
        self.list.SetColumnWidth(2, 92)

        # 添加一组按钮，实现增删改查,用一个panel来管理该组按钮的布局
        self.panel = wx.Panel(self, pos=(0, 300), size=(400, 100))

        # 定义一组按钮
        add_button = wx.Button(self.panel, label="添加", pos=(10, 15), size=(60, 30))  # , size = (75, 30)
        del_button = wx.Button(self.panel, label="删除", pos=(110, 15), size=(60, 30))  # , size = (75, 30)
        update_button = wx.Button(self.panel, label="修改", pos=(210, 15), size=(60, 30))  # , size = (75, 30)
        query_button = wx.Button(self.panel, label="查看", pos=(310, 15), size=(60, 30))  # , size = (75, 30)
        # w为按钮绑定相应事件函数，第一个参数为默认参数，指明为按钮类事件，第二个为事件函数名，第三个为按钮名
        self.Bind(wx.EVT_BUTTON, self.addBook, add_button)
        self.Bind(wx.EVT_BUTTON, self.delBook, del_button)
        self.Bind(wx.EVT_BUTTON, self.updateBook, update_button)
        self.Bind(wx.EVT_BUTTON, self.queryBook, query_button)

        # 将列表和panel添加到主面板
        self.main_layout.Add(self.list, 3)
        self.main_layout.Add(self.panel, 1)

        self.SetSizer(self.main_layout)

        # 添加数据库操作对象
        self.dbhelper = DBHelper()
        datas = self.dbhelper.getAllBook()

        for data in datas:
            index = self.list.InsertItem(self.list.GetItemCount(), str(data[0]))
            self.list.SetItem(index, 1, data[1])
            self.list.SetItem(index, 2, data[2])

    def addBook(self, evt):
        '''添加书籍按钮，弹出添加书籍框'''
        add_f = AddFrame(self, "添加书籍窗口")
        add_f.Show(True)

    def delBook(self, evt):
        '''删除书籍按钮，先选中,然后删除'''
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message="未选中任何条目！！！", caption="错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            bookid = self.list.GetItem(selectId, 0).Text  # 得到书本id
            self.list.DeleteItem(selectId)  # 先在listctrl中删除选中行
            self.dbhelper.deleteBook(bookid)

    def updateBook(self, evt):
        '''修改按钮响应事件，点击修改按钮，弹出修改框'''
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message="未选中任何条目！！！", caption="错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            update_f = UpdateFrame(self, "修改书籍窗口", selectId)
            update_f.Show(True)

    def queryBook(self, evt):
        '''查看按钮响应事件'''
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message="未选中任何条目！！！", caption="错误警告", style=wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()  # 提示错误
            warn.Destroy()
            return
        else:
            show_f = ShowFrame(self, "修改书籍窗口", selectId)
            show_f.Show(True)

    def addToList(self, id, book):
        index = self.list.InsertItem(self.list.GetItemCount(), str(id))
        self.list.SetItem(index, 1, book.getBookName())
        self.list.SetItem(index, 2, str(book.getAddDate()))


AppBaseClass = wx.App


class LibraryApp(AppBaseClass):
    def OnInit(self):
        frame = LibraryFrame(None, "library-system")
        frame.Show()

        return True


# 类似于c中的main函数，但被其他模块导入时，__name__值不是"__main__"
if __name__ == "__main__":
    app = LibraryApp()
    app.MainLoop()
