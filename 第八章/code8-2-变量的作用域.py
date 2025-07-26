# 全局变量
num = 1
list1 = [1,2,3,4,5]
map1 = {'name':'张三'}
# 定义一个函数
def f():
    num2 = 2
    print('在函数里面调用num2=', num2)
    # 修改num的值 如果要全局修改，得先声明
    global num
    num = 8
    print('在函数里面调用num=', num)
    # 修改list1的值
    list1[2] = 9
    print('f中修改之后list1的值', list1)
    # 修改字典的值
    map1['age'] = 19
    print('map1:', map1)

f()
# 打印num
print('num=', num)
print('list1=', list1)
print('map1:', map1)