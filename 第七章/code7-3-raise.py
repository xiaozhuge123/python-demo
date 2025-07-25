try:
    num = int(input('请输入一个数：'))
    if num == 0:
        raise Exception('不能输入0')
    sum = 100 / num
except Exception as e:
    print('计算错误',e)
else:
    print('计算无误')
finally:
    print('不管计算结果都执行')