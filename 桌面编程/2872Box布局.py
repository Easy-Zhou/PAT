#!/anaconda3/bin/python
# @Time    : 2019-04-21 17:10
# @Author  : zhou
# @File    : 2872Box布局
# @Software: PyCharm
# @Description: 

import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title='Box布局',
            size=(300, 200))
        self.Center()
        panel = wx.Panel(parent=self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.text = wx.StaticText(panel, label="Hello")
        bt1 = wx.Button(panel, id=1, label="Button1")
        bt2 = wx.Button(panel, id=2, label="Button2")
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)
        hbox.Add(bt1, proportion=1, flag=wx.ALIGN_CENTER | wx.EXPAND)
        hbox.Add(bt2, proportion=1, flag=wx.ALIGN_CENTER | wx.EXPAND)
        vbox.Add(self.text, proportion=1, flag=wx.ALIGN_CENTER)
        vbox.Add(hbox, proportion=1, flag=wx.ALIGN_CENTER | wx.EXPAND)
        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 1:
            self.text.SetLabel("Button1单击")
            self.text.SetPosition((110,0))
        else:
            self.text.SetLabel("Button2单击")
            self.text.SetPosition((110, 0))


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
