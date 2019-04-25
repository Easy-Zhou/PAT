import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title="FlexGrid布局",
                         size=(400, 300),
                         )
        self.Center()
        panel = wx.Panel(self)
        st1 = wx.StaticText(panel, label="标题：")
        st2 = wx.StaticText(panel, label="作者：")
        st3 = wx.StaticText(panel, label="内容：")
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        grid = wx.FlexGridSizer(3, 2, 10, 10)
        grid.AddMany([
            st1, (tc1, 1, wx.EXPAND),
            st2, (tc2, 1, wx.EXPAND),
            st3, (tc3, 1, wx.EXPAND),
        ])

        grid.AddGrowableRow(0, 1)
        grid.AddGrowableRow(1, 1)
        grid.AddGrowableRow(2, 3)
        grid.AddGrowableCol(0, 1)
        grid.AddGrowableCol(1, 2)

        hbox = wx.BoxSizer()
        hbox.Add(grid, 1, flag=wx.ALL | wx.EXPAND, border=20)

        panel.SetSizer(hbox)


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
