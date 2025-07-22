i = 0
while i < 10:
    if i == 2:
        print(i)
        break
    i += 1
print('over')

# 与else结合使用
num = 1
sum = 0
while num <= 30:
    sum += num
    if sum == 10:
        print('sum=10')
        break
    num += 1
else:
    print('没有执行break语句')