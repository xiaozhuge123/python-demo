import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8888))

# 发送内容到服务器
while True:
    data = input('请输入你要发送的内容：')
    sk.send(data.encode('utf-8'))
    redata = sk.recv(1024)
    print(redata.decode('utf-8'))