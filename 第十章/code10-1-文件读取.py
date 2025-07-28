# 打开文件
# f = open('test.txt')
# 绝对路径
import os
url = os.getcwd()
filename = url + '/test.txt'
f = open(filename,mode='r',encoding='utf-8')
# 读取文件
t = f.read(5)
print(t)
# 关闭文件
f.close()