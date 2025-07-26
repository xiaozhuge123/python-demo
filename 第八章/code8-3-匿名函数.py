f = lambda x, y: x + y
print(f(1,2))

# 函数名作为参数
def func(x,y):
    return x + y
f = func
print(f(1,2))