# 上阶梯的方法数，每次可以上1阶或2阶
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n - 1) + f(n - 2)
print('上%d阶楼梯有%d种方式' % (10,f(10)))
print('*' * 20)

# 循环的方式解决
a = [0,1,2]
for i in range(3,11):
    a.append(a[i-1] + a[i-2])
    print('上%d阶楼梯有%d种方式' % (i, a[-1]))