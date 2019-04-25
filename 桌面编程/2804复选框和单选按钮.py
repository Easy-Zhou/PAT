#!/anaconda3/bin/python
# @Time    : 2019-04-21 15:14
# @Author  : zhou
# @File    : 2804复选框和单选按钮
# @Software: PyCharm
# @Description: 


import wx


class MyFrame(wx.Frame):

    info = ["Python","Java","C++"]
    mark = ["","Java",""]
    def __init__(self):
        super().__init__(
            parent=None,
            title=' 复选框和单选按钮',
            size=(400, 300))
        self.Center()
        # 设置左上角图标，photo.ico是同一文件下的图片名
        self.icon = wx.Icon('icon/dog4.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        panel = wx.Panel(parent=self)
        self.s = "准备就绪"
        self.statusBar = wx.StatusBar(self, -1)
        self.statusBar.SetFieldsCount(1)
        self.statusBar.SetStatusText(self.s)
        self.SetStatusBar(self.statusBar)

        text1 = wx.StaticText(panel, -1, "选择你喜欢的编程语言：", pos=(10, 20))
        self.cb1 = wx.CheckBox(panel, -1, "Python", pos=(150, 20))
        self.cb2 = wx.CheckBox(panel, -1, "Java", pos=(220, 20))
        self.cb2.SetValue(True)
        self.cb3 = wx.CheckBox(panel, -1, "C++", pos=(290, 20))
        text2 = wx.StaticText(panel, -1, "选择性别：", pos=(10, 80))
        rb1 = wx.RadioButton(panel, -1, "男", pos=(150, 80), style=wx.RB_GROUP)
        rb2 = wx.RadioButton(panel, -1, "女", pos=(250, 80))
        text3 = wx.StaticText(panel, -1, "选择你喜欢吃的水果：", pos=(10, 140))
        lst = ["苹果", "橘子", "香蕉"]
        self.rbox = wx.RadioBox(panel, -1, "", pos=(150, 130), choices=lst,
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.OnRadiobox)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.cb1)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.cb2)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.cb3)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)

    def doMe(self):
        self.Destroy()

    def EvtCheckBox(self, event):
        cb = event.GetEventObject()
        label = str(cb.GetLabel())
        if cb.GetValue():
            if label in self.info:
                index = self.info.index(label)
                self.mark[index] = label
        else:
            if label in self.info:
                index = self.info.index(label)
                self.mark[index] = ""
        temp = []
        for i in self.mark:
            if len(i) > 0:
                temp.append(i)
        self.s = '第零组 ' + ",".join(temp) + ' 被选中'
        self.statusBar.SetStatusText(self.s)

    def OnRadiogroup(self, event):
        rb = event.GetEventObject()
        self.s = '第一组 ' + str(rb.GetLabel()) + ' 被选中'
        self.statusBar.SetStatusText(self.s)

    def OnRadiobox(self, event):
        self.s = "第二组 " + str(self.rbox.GetStringSelection()) + " 被选中"
        self.statusBar.SetStatusText(self.s)


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
