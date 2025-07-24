info_tuple = (1,2,3,4,5)
print(info_tuple)

# 创建元组
t1 = ()
print(t1,type(t1))

t2 = (1,2,3,4,5)
print(t2)

# 创建只有一个元素的元组，需要在元素后面添加一个,号
t3 = (1,)
print(t3,type(t3))

t3 = (1,4,5,True,'hello')
t4 = 10,20,30
print(t4,type(t4))

t5 = tuple('hello')
print(t5,type(t5))

# 元组元素的访问
t4 = 1,2,3,4,5
print(t4[2])
# print(t4[8])
print(t4[-1])
print('*' * 20)
t5 = (1,2,3,4,5,[6,7,8])
t5[5][1] = 90
print(t5)
print('*' * 20)

# 元组对称赋值
# 用于函数返回多个返回值
num1,num2 = (1,2)
print('num1 = %d' % num1)
print('num2 = %d' % num2)
print('*' * 20)

# 通用操作
# 连接
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)
# 重复
print(t1 * 2)
# 切片
print(t3[0:3])
print(t3[3:])
print(t3[-1::-1])
# 成员运算符
print(3 in t3)
print(2 not in t3)
# 元素个数
print(len(t3))
# 最大值
print(max(t3))
# 最小值
print(min(t3))

# 元组和列表的转换
t1 = (1,2,3)
l1 = [4,5,6]
# 列表转元组
print(tuple(l1))
# 元组转列表
print(list(t1))

# 元组常用操作
t1 = (1,2,3)
print(t1.index(3))
print(t1.count(3))
# print(t1.index(4))
# print(t1.count(4))
print('*' * 20)
# 循环遍历
t1 = (1,2,3)
for item in t1:
    print(item)
print('*' * 20)
for item,value in enumerate(t1):
    print(item,value)
print('*' * 20)
# 通过下标遍历
for i in range(len(t1)):
    print(t1[i])
print('*' * 20)

info = ('zhangsan',10)
print('%s 的年龄是 %d' %info)
print('*' * 20)

# 二维元组
t1 = ((1,2,3),(4,5,6))
for item in t1:
    for value in item:
        print(value,end=' ')
    print('')
print('*' * 20)

# 元组解包
# 变量个数和元素个数一致
t1 = (11,20)
a,b = t1
print(a,b)
print('*' * 20)

a,b = 2,3
a,b,c = (7,8,9)
print(a,b,c)
print('*' * 20)

# 元素个数和变量个数不相同
a,*_,c = 10,20,30,40
print(a,c,_)
print('*' * 20)

a,b,*c = 10,20,30,40,50
print(a,b,c)
print('*' * 20)

# *解包
print(*(1,2,3))

# range解包
a,b,c = range(3)
print(a,b,c)

# 列表解包
a,*_b,c = [3,4,5,676,76,8,68]
print(a,_b,c)

# 字符串解包
a,b,c = 'hel'
print(a,b,c)
