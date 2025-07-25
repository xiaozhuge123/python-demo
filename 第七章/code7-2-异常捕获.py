try:
    num = int(input('请输入一个数：'))
    sum = 100 / num
except:
    print('计算错误')
else:
    print('计算无误')
finally:
    print('不管计算结果都执行')