#!/anaconda3/bin/python
# @Time    : 2019-04-28 16:41
# @Author  : zhou
# @File    : 1822_qq简易聊天(server)
# @Software: PyCharm
# @Description:

import wx
import socket


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title="qq简易聊天，服务端",
                         size=(400, 300),
                         pos=(100, 100))

        self.bkg = wx.Panel(self)  # 将控件放在Panel上，而不是直接放在frame上

        self.tshow = wx.TextCtrl(self.bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

        self.tinput = wx.TextCtrl(self.bkg)
        self.bt = wx.Button(self.bkg, label="发送")

        self.box1 = wx.BoxSizer()
        self.box1.Add(self.tinput, proportion=1, flag=wx.EXPAND)
        self.box1.Add(self.bt, proportion=0)

        self.box2 = wx.BoxSizer(wx.VERTICAL)
        self.box2.Add(self.tshow, flag=wx.EXPAND | wx.ALL, border=5, proportion=1)
        self.box2.Add(self.box1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5,
                      proportion=0)  # 把第一个BoxSiSizer放入整体Boxizer

        self.bkg.SetSizer(self.box2)

        self.bt.Bind(wx.EVT_BUTTON, self.btaction)  # 为控件绑定事件和处理函数

    def btaction(self, event):
        self.tshow.AppendText(self.tinput.GetValue() + "\n")
        self.tinput.SetValue("")


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

