# 方式一：全部导入，包括方法和全局变量
# import my_module
# print(my_module.add(1, 2))
# print(my_module.sub(1, 2))
# print(my_module.author)

# 方式二：按需导入,调用时不用加模块名
# from my_module import author,add
# print(author)
# print(add(1,2))

# 方式三：导入所有，调用不用加模块名
# from my_module import *
# print(author)
# print(add(1,2))
# print(sub(1,2,3,4,5,6))

# 方式四：导入方法改名称
from my_package.my_math import add as f
print(f(1,2))
