import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title = 'python学习系统',size=(800,600),pos=(100,100))
        pl = wx.Panel(self, size=(300, 200), pos=(50, 60))
        st = wx.StaticText(pl, label='hello', pos=(20, 30))
        btn = wx.Button(pl, label='按钮1')

app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()