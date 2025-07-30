from threading import main_thread

import wx
from socket import *
import threading
from faker import Faker

class Client(wx.Frame):
    # 构造方法
    def __init__(self):
        # 实例属性
        self.name = Faker('zh_CN').name() # 客户端的名字
        self.isConnected = False # 客户端是否连接服务器
        self.client_socket = None
        wx.Frame.__init__(self, None, title=self.name + '聊天客户端', pos=(100, 50), size=(450, 660))
        self.pl = wx.Panel(self)
        self.conn_btn = wx.Button(self.pl,label='加入聊天室',pos=(10,10),size=(200,40))
        self.dis_conn_btn = wx.Button(self.pl, label='离开聊天室', pos=(220, 10), size=(200, 40))
        self.clear_btn = wx.Button(self.pl, label='清空', pos=(10, 580), size=(200, 40))
        self.send_btn = wx.Button(self.pl, label='发送', pos=(220, 580), size=(200, 40))

        self.text = wx.TextCtrl(self.pl,size = (400,400),pos = (10,60), style=wx.TE_READONLY|wx.TE_MULTILINE)
        self.input_text = wx.TextCtrl(self.pl, size=(400, 100), pos=(10, 470), style=wx.TE_MULTILINE)

        # 事件绑定
        self.Bind(wx.EVT_BUTTON, self.conn, self.conn_btn)
        self.Bind(wx.EVT_BUTTON, self.dis_conn, self.dis_conn_btn)
        self.Bind(wx.EVT_BUTTON, self.clear, self.clear_btn)
        self.Bind(wx.EVT_BUTTON, self.send, self.send_btn)

    def conn(self, event):
        if not self.isConnected:
            self.isConnected = True
            self.client_socket = socket()
            self.client_socket.connect(('127.0.0.1',8999))
            # 发送一条信息
            self.client_socket.send(self.name.encode('utf-8'))

            main_thread = threading.Thread(target=self.recv_data)
            main_thread.daemon = True
            main_thread.start()

    def recv_data(self):
        while self.isConnected:
            text = self.client_socket.recv(1024).decode('utf-8')
            self.text.AppendText(text + '\n')

    def dis_conn(self, event):
        self.client_socket.send('断开连接'.encode('utf-8'))
        self.isConnected = False

    def clear(self, event):
        self.input_text.Clear()

    def send(self, event):
        if self.isConnected:
            text = self.input_text.GetValue()
            if text != '':
                self.client_socket.send(text.encode('utf-8'))
                self.input_text.Clear()

if __name__ == '__main__':
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()
