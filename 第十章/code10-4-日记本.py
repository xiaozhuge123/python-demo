def write_text():
    filename = '日记本.txt'
    date = input('请输入日期：')
    context = input('请输入内容：')
    # f = open(filename,mode='a',encoding='utf-8')
    # f.write('asdf\n')
    # f.write(date + '\n')
    # f.write(context + '\n')
    # f.close()

    with open(filename, mode='a', encoding='utf-8') as f:
        f.write('asdf\n')
        f.write(date + '\n')
        f.write(context + '\n')

def read_text(day):
    filename = '日记本.txt'
    # f = open(filename, mode='r', encoding='utf-8')
    # content = f.read()
    # f.close()
    with open(filename, mode='r', encoding='utf-8') as f:
        content = f.read()
    if day != -1:
        lista = content.split('asdf\n')
        for i in lista:
            if day == i[:8]:
                return i
    else:
        print(content.replace('asdf\n',''))



def quit():
    print('欢迎再次使用')

def mune():
    print('''
        欢迎来到日记系统：
        1：记录日记
        2：读取日记
        3：退出系统
    ''')

mune()
while True:
    op = input('请输入你的选择：')
    if op == '1':
        write_text()
    elif op == '2':
        date = input('请输入你要查询的日期：')
        text = read_text(date)
        if text:
            print(text)
        else:
            print('未查询到日记')
    elif op == '3':
        quit()
        break
    else:
        print('请重新输入你的选择')
