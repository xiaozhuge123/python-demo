x = input('请输入数字：')
if x.isdigit():
    x = int(x)
    match x:
        case 1:
            print('x is 1')
        case 2:
            print('x is 2')
        case _:
            print('other')
else:
    print('请输入数字')