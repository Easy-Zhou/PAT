#!/anaconda3/bin/python
# @Time    : 2019-04-21 16:47
# @Author  : zhou
# @File    : 2869
# @Software: PyCharm
# @Description: 


import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title='分隔窗口',
            size=(400, 300))
        self.Center()

        splitter = wx.SplitterWindow(self, -1)
        panel1 = wx.Panel(splitter, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.StaticText(panel1, label="右侧面板")
        hbox.Add(self.text, 1)

        panel1.SetSizerAndFit(hbox)
        panel2 = wx.Panel(splitter, -1)

        self.languages = ['苹果', '橘子', '香蕉']
        lst = wx.ListBox(panel2, size=(100, 250), choices=self.languages, style=wx.LB_SINGLE)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(lst, 1)

        panel2.SetSizer(hbox1)
        splitter.SplitVertically(panel2, panel1, sashPosition=100)
        self.Centre()
        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)
        self.Show(True)

    def onListBox(self, event):
        s = "选择 " + str(self.languages[event.GetEventObject().GetSelection()])
        self.text.SetLabel(s)


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
