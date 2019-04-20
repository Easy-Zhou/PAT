import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title="First",
                         size=(400,300),
                         pos=(100,100))


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