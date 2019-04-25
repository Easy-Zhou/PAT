#!/anaconda3/bin/python
# @Time    : 2019-04-21 16:10
# @Author  : zhou
# @File    : 2805下拉列表
# @Software: PyCharm
# @Description: 

import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title='下拉列表',
            size=(400, 300))
        self.Center()
        panel = wx.Panel(parent=self)
        self.s = "准备就绪"
        self.statusBar = wx.StatusBar(self, -1)
        self.statusBar.SetFieldsCount(1)
        self.statusBar.SetStatusText(self.s)
        self.SetStatusBar(self.statusBar)

        text1 = wx.StaticText(panel, -1, "选择你喜欢的编程语言:", pos=(10, 20))
        lst = ['Python', 'Java', 'C++']
        self.cmb = wx.ComboBox(panel, value="C++", choices=lst, pos=(200, 20), size=(150, 60))
        self.Bind(wx.EVT_COMBOBOX, self.ComboBoxFunc, self.cmb)

        text2 = wx.StaticText(panel, -1, "选择性别:", pos=(10, 150))
        self.sex = ['男', '女']
        self.chooseSex = wx.Choice(panel, -1, choices=self.sex, pos=(200, 150), size=(150, 60))
        self.chooseSex.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.ChooseFunc, self.chooseSex)

    def ChooseFunc(self, e):
        ch = e.GetEventObject().GetSelection()
        self.s = "选择 " + str(self.sex[ch])
        self.statusBar.SetStatusText(self.s)

    def ComboBoxFunc(self, e):
        co = e.GetEventObject()
        self.s = "选择 " + str(co.GetValue())
        self.statusBar.SetStatusText(self.s)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('exit')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
