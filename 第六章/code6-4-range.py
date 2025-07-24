print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(0,10,2)))

# 计算高斯求和
sum = 0
for i in range(101):
    sum += i
print(sum)
print('*' * 20)

# 兔子问题
one = 1
two = 0
threes = 1
for i in range(4,20):
    threes = threes + two
    two = one
    one = threes
    print(one + two + threes)
print('*' * 20)

# 水仙花数
for i in range(100,1000):
    a = i % 10
    b = i / 10 % 10
    c = i // 100
    if i == a ** 3 + b ** 3 + c ** 3:
        print(a,b,c)
        print(i)

# 猴子吃桃
x2 = 1
x1 = 0
for i in range(9,0,-1):
    x1 = (x2 +1) * 2
    x2 = x1
print(x1)


