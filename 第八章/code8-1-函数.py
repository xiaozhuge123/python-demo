# 定义函数
def sum_1(a,b)->int:
    return a+b

def str1(a) -> str:
    return 'hello world' + a
# 函数调用
value = sum_1(5,6)
print(value)

print(str1('123'))
print('*' * 20)

# 定义 默认参数 缺省参数 位置参数
def infos(name, age = 24, gender = '男'):
    return '我是%s,今年%d,是一个%s生' % (name, age, gender)

# 位置参数
s1 = infos('张三',25,'男')
print(s1)
# 默认参数
s2 = infos('李四')
print(s2)
# 缺省参数
s3 = infos('王五', 29)
print(s3)
s4 = infos('赵六', gender = '女')
print(s4)
print('*' * 20)

# 可变参数
def f1(*args):
    print(args)
    result = 0
    for i in args:
        result += i
    return result
# 调用可变参数方式一
result = f1(1,2,3,4,5)
print(result)
# 调用可变参数方式二
s = [1,2,3,4,5]
result = f1(*s)
print(result)

# 可变参数-字典
def f2(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
    return 1
# 调用字典可变函数
z = {'name':'张三','age':30}
result = f2(**z)
print(result)
result = f2(**{'name':'sdfgrdg'})
print(result)
