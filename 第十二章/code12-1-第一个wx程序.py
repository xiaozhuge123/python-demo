from cProfile import label

import wx

def onClick(event):
    print("点击了按钮")

# 创建应用程序对象
app = wx.App()

# 创建窗口
frm = wx.Frame(None,title = 'python学习系统',size=(800,600),pos=(100,100))
# 显示窗口
frm.Show()

# 创建面板
pl = wx.Panel(frm,size=(300,200),pos=(50,60))
# 显示面板
pl.Show(True)

# 创建静态文本
st = wx.StaticText(pl,label = 'hello',pos=(50,60))
st.Show(True)

# 创建按钮
btn = wx.Button(pl,label = '按钮1')
btn.Show(True)
frm.Bind(wx.EVT_BUTTON,onClick,btn)


# 进入主循环，让窗口一直显示
app.MainLoop()