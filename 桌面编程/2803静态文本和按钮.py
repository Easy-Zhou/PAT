#!/anaconda3/bin/python
# @Time    : 2019-04-21 14:35
# @Author  : zhou
# @File    : 2803静态文本和按钮
# @Software: PyCharm
# @Description: 

import wx


class MyFrame(wx.Frame):
    bts = []

    def __init__(self):
        super().__init__(
            parent=None,
            title=' Grid布局',
            size=(300, 300))
        self.Center()
        panel = wx.Panel(parent=self)
        for i in range(1, 10):
            self.bts.append((wx.Button(panel, id=i, label=str(i)), i, wx.EXPAND))

        grid = wx.FlexGridSizer(3, 3, 0, 0)
        grid.AddMany(self.bts)

        grid.AddGrowableRow(0, 1)
        grid.AddGrowableRow(1, 1)
        grid.AddGrowableRow(2, 1)
        grid.AddGrowableCol(0, 1)
        grid.AddGrowableCol(1, 1)
        grid.AddGrowableCol(2, 1)

        hbox = wx.BoxSizer()
        hbox.Add(grid, 1, flag=wx.ALL | wx.EXPAND)

        panel.SetSizer(hbox)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print(' exit')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
