#!/anaconda3/bin/python
# @Time    : 2019-04-21 14:09
# @Author  : zhou
# @File    : 2875-网格(二)
# @Software: PyCharm
# @Description:


import wx
import wx.grid


class SimpleGrid(wx.grid.Grid):
    info = [("0036", "高等数学", "李放", "人民邮电出版社", "20000812", "1"),
            ("0004", "FLASH精选", "刘杨", "中国纺织出版社", "19990312", "2"),
            ("0026", "软件工程", "牛田", "经济科学出版社", "20000328", "4"),
            ("0015", "人工智能", "周末", "机械工业出版社", "19991223", "3"),
            ]

    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(4, 6)
        self.SetColLabelValue(0, "书籍编号")
        self.SetColLabelValue(1, "书籍名称")
        self.SetColLabelValue(2, "作者")
        self.SetColLabelValue(3, "出版社")
        self.SetColLabelValue(4, "出版日期")
        self.SetColLabelValue(5, "库存数量")

        for i in range(1, 5):
            self.SetRowLabelValue(i - 1, str(i))
            for j in range(6):
                self.SetCellValue(i - 1, j, self.info[i - 1][j])
                self.SetCellAlignment(i - 1, j, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                if (i - 1) % 2 == 0:
                    color = wx.GREEN
                else:
                    color = wx.BLUE
                self.SetCellBackgroundColour(i - 1, j, color)

        self.AutoSize()


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title="网格控件",
                         size=(500, 200),
                         )

        self.Center()
        grid = SimpleGrid(self)


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
