#!/anaconda3/bin/python
# @Time    : 2019-04-21 16:22
# @Author  : zhou
# @File    : 静态图片控件
# @Software: PyCharm
# @Description: 


import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title='静态图片控件',
            size=(400, 300))
        self.Center()
        self.panel = wx.Panel(parent=self)

        self.bmps = [wx.Bitmap('images/bird5.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('images/bird4.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('images/bird3.gif', wx.BITMAP_TYPE_GIF)
                     ]
        bt1 = wx.Button(self.panel, id=1, label="Button1")
        bt2 = wx.Button(self.panel, id=2, label="Button2")
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)
        self.image = wx.StaticBitmap(self.panel, -1, self.bmps[0])
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(bt1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(bt2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(self.image, proportion=3, flag=wx.CENTER | wx.EXPAND)
        self.panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 1:
            self.image.SetBitmap(self.bmps[1])
        else:
            self.image.SetBitmap(self.bmps[2])
        self.panel.Layout()


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
