num = input('请输入三个整数，使用空格隔开：').split()
num.sort()
num1,num2,num3 = int(num[0]),int(num[1]),int(num[2])
if num1 + num2 > num3:
    if num1 ** 2 + num2 ** 2 == num3 ** 2:
        print('直角三角形')
    elif num1 ** 2 + num2 ** 2 > num3 ** 2:
        print('锐角三角形')
    else:
        print('钝角三角形')
    if num1 == num2 or num2 == num3:
        print('等腰三角形')
    if num1 == num2 and num2 == num3:
        print('等边三角形')
else:
    print('不能组成三角形')


