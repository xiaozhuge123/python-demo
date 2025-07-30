import wx
from socket import *
import threading
from concurrent.futures import ThreadPoolExecutor

class Server(wx.Frame):
    def __init__(self):
        self.isOn = False
        self.server_socket = socket()
        self.server_socket.bind(('0.0.0.0',8999))
        self.server_socket.listen(5)
        self.client_thread_dict = {}
        self.pool = ThreadPoolExecutor(max_workers = 10)

        wx.Frame.__init__(self, None, title='多人聊天室', pos=(0, 50), size=(450, 660))
        self.pl = wx.Panel(self)

        # 设置按钮
        self.start_server_btn = wx.Button(self.pl,pos=(10,10),size=(200,40),label='启动服务器')
        self.save_text_btn = wx.Button(self.pl, pos=(220, 10), size=(200, 40), label='保存聊天记录')
        self.text = wx.TextCtrl(self.pl, size=(400, 400), pos=(10, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)

        self.Bind(wx.EVT_BUTTON, self.start_server, self.start_server_btn)
        self.Bind(wx.EVT_BUTTON, self.save_text, self.save_text_btn)

    def start_server(self,event):
        if not self.isOn:
            self.isOn = True
            # 创建线程
            main_thread = threading.Thread(target=self.main_thread_fun)
            # 设置为守护线程
            main_thread.daemon = True
            main_thread.start()

    def main_thread_fun(self):
        while self.isOn:
            client_socket,client_addr = self.server_socket.accept()
            print(client_addr)
            client_name = client_socket.recv(1024).decode('utf-8')
            print(client_name)
            client_thread = ClientThread(client_socket, client_name,self)
            # 保存到客户端
            self.client_thread_dict[client_name] = client_thread
            self.pool.submit(client_thread.run)
            self.send('【服务器通知】欢迎%s进入聊天室' % client_name)

    def send(self,text):
        self.text.AppendText(text + '\n')
        for client in self.client_thread_dict.values():
            if client.isOn:
                client.client_socket.send(text.encode('utf-8'))

    def save_text(self,event):
        record = self.text.GetValue()
        with open('record.log','a+',encoding='utf-8') as f:
            f.write(record)


class ClientThread(threading.Thread):
    def __init__(self,socket,name,server):
        threading.Thread.__init__(self)
        self.client_socket = socket
        self.client_name = name
        self.server = server
        self.isOn = True

    def run(self):
        while self.isOn:
            text = self.client_socket.recv(1024).decode('utf-8')
            if text == '断开连接':
                self.isOn = False
                self.server.send('【服务器消息】%s离开了聊天室' % self.client_name)
            else:
                self.server.send('【%s】%s' %(self.client_name,text))
        self.client_socket.close()

if __name__ == '__main__':
    app = wx.App()
    server = Server()
    server.Show()
    app.MainLoop()