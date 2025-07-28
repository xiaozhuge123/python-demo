import socket

sk = socket.socket()
# 绑定ip和端口
sk.bind(('127.0.0.1', 8888))
# 监听客户端数量
sk.listen(5)

# 等待客户端连接
conn, addr = sk.accept()
print(conn)
print(addr)
while True:
    data = conn.recv(1024)
    print(data.decode('utf-8'))
    redata = '收到消息'
    conn.send(redata.encode('utf-8'))
