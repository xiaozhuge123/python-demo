for n in range(10):
    if n == 2:
        continue
    print('x = %d' %n)
print('*' * 20)

sum = 0
for n in range(1,3):
    sum += n
    if sum == 10:
        print('sum=10')
        break
    if 1:
        print('pass')
        pass
    n += 1
else:
    print('sum!=10')
