#!/anaconda3/bin/python
# @Time    : 2019-04-21 16:20
# @Author  : zhou
# @File    : 2850列表
# @Software: PyCharm
# @Description: 


import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title='列表',
            size=(400, 300))
        self.Center()
        panel = wx.Panel(parent=self)

        text1 = wx.StaticText(panel, -1, "选择你喜欢的编程语言:", pos=(10, 20))
        lst = ['Python', 'C++', 'Java']
        self.lst1 = wx.ListBox(panel, choices=lst, pos=(200, 20), size=(120, 70), style=wx.LB_SINGLE)

        text2 = wx.StaticText(panel, -1, "选择你喜欢吃的水果:", pos=(10, 150))
        self.fruit = ['苹果', '橘子', '香蕉']
        self.lst2 = wx.ListBox(panel, -1, choices=self.fruit, pos=(200, 150), size=(120, 70), style=wx.LB_MULTIPLE)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print(' 应用程序退出')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()

