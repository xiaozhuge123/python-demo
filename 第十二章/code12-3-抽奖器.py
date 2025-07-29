import wx
import random

class MyFrame(wx.Frame):
    # 抽奖列表
    name_list = ['tom','jack','jim']
    def __init__(self):
        wx.Frame.__init__(self,None,title = '抽奖器',pos = (100,100),size = (400,600))
        self.pl = wx.Panel(self,pos = (0,0),size = (400,600))
        # 设置背景颜色
        self.SetBackgroundColour(wx.Colour(25,230,135))
        self.st = wx.StaticText(self.pl, label=random.choice(self.name_list),pos = (0,50),size=(100,400),style=wx.ALIGN_RIGHT)
        # 设置字体
        font = wx.Font(29, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.NORMAL)
        self.st.SetFont(font)
        self.btn = wx.Button(self.pl, label='开始抽奖', pos=(100, 160))
        self.btn_end = wx.Button(self.pl, label='结束抽奖', pos=(200, 160))
        # 绑定点击事件
        self.Bind(wx.EVT_BUTTON, self.onClick, self.btn)
        self.Bind(wx.EVT_BUTTON, self.stop, self.btn_end)

    def onClick(self, event):
        # 设置定时器
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_name, self.timer)
        self.timer.Start(100)

    def update_name(self, event):
        self.st.SetLabelText(random.choice(self.name_list))

    def stop(self, event):
        self.timer.Stop() # 停止计时器

if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame()
    frm.Show()
    app.MainLoop()