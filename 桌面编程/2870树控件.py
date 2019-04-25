#!/anaconda3/bin/python
# @Time    : 2019-04-21 16:57
# @Author  : zhou
# @File    : 2870树控件
# @Software: PyCharm
# @Description: 

import wx


class MyFrame(wx.Frame):
    items = []

    def __init__(self):
        super().__init__(parent=None, title="树控件", size=(500, 400))
        self.Center()
        swindow = wx.SplitterWindow(parent=self, id=-1)
        left = wx.Panel(parent=swindow)
        right = wx.Panel(parent=swindow)

        swindow.SplitVertically(left, right, 200)
        swindow.SetMinimumPaneSize(80)

        self.tree = self.CreateTreeCtrl(left)
        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_click, self.tree)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        left.SetSizer(vbox1)
        vbox1.Add(self.tree, 1, flag=wx.EXPAND | wx.ALL, border=5)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        right.SetSizer((vbox2))
        self.st = wx.StaticText(right, 2, label='右侧面板')
        vbox2.Add(self.st, 1, flag=wx.EXPAND | wx.ALL, border=5)

    def on_click(self, event):
        item = event.GetItem()
        self.st.SetLabel(self.tree.GetItemText(item))

    def CreateTreeCtrl(self, parent):
        tree = wx.TreeCtrl(parent)
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, size=(16, 16)))
        tree.AssignImageList(imglist)
        root = tree.AddRoot('TreeRoot', image=0)
        for i in range(1, 6):
            self.items.append(tree.AppendItem(root, 'Item' + str(i), 0))
        tree.Expand(root)
        tree.SelectItem(root)

        for item in self.items:
            for j in range(1,6):
                tree.AppendItem(item, 'Subitem' +str(j), 1)
                tree.Expand(item)

        return tree


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
