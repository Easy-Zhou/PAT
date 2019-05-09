#!/anaconda3/bin/python
# @Time    : 2019-04-28 16:41
# @Author  : zhou
# @File    :
# @Software: PyCharm
# @Description:

import wx
import socket
import threading
import math


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title="Server",
                         size=(400, 300),
                         pos=(100, 100))
        self.bkg = wx.Panel(self)  # 将控件放在Panel上，而不是直接放在frame上

        self.tshow = wx.TextCtrl(self.bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

        # self.tinput = wx.TextCtrl(self.bkg)
        # self.bt = wx.Button(self.bkg, label="发送")

        # self.box1 = wx.BoxSizer()
        # self.box1.Add(self.tinput, proportion=1, flag=wx.EXPAND)
        # self.box1.Add(self.bt, proportion=0)

        self.box2 = wx.BoxSizer(wx.VERTICAL)
        self.box2.Add(self.tshow, flag=wx.EXPAND | wx.ALL, border=5, proportion=1)
        # self.box2.Add(self.box1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5,
        #               proportion=0)  # 把第一个BoxSiSizer放入整体Boxizer

        self.bkg.SetSizer(self.box2)

        # self.bt.Bind(wx.EVT_BUTTON, self.btaction)  # 为控件绑定事件和处理函数

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind(('localhost',3334))
        self.serverSocket.listen(1)
        self.clientSocket, addr = self.serverSocket.accept()

    def listenClient(self):
        while True:
            msg = self.clientSocket.recv(1024).decode('utf-8')
            self.tshow.AppendText('Radius received from client：' + msg + '\n')
            area = math.pi * float(msg)** 2
            self.tshow.AppendText('Area is：' + str(area) + '\n')
            self.clientSocket.send(str(area).encode('utf-8'))


    # def btaction(self, event):
    #     msg = self.tinput.GetValue()
    #     self.tshow.AppendText('服务器端 对 客户端 说：'+ msg + "\n")
    #     # self.clientSocket.send(msg.encode('utf-8'))
    #     self.tinput.SetValue("")

    def __del__(self):
        self.clientSocket.close()
        self.serverSocket.close()

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        lis = threading.Thread(target=frame.listenClient)
        lis.start()
        return True

    def OnExit(self):
        print("exit")
        return 0


if __name__ == "__main__":
    app = App()
    app.MainLoop()

