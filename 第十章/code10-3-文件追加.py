# 打开文件
f = open('test.txt',mode='a',encoding='utf-8')
# 写入内容
f.write('我在写入文件\n')
f.writelines(['sdjh','sfsdgf'])
# 关闭文件
f.close()