age = 10
name = 'hello'
print(type(age),type(name))
print(isinstance(age,int),isinstance(name,str))
print('=' * 20)

# 整型
num1 = 10
print(num1)
print(type(num1))
print('=' * 20)

# 浮点型
num1 = 0.123454
num2 = 3.14
print(num1 + num2)
print(type(num1 + num2))
print('=' * 20)

# 布尔型
a = True
b = False
print(type(a),type(b))
print(a,b)
print('=' * 20)

# 字符串
# 单引号字符串
str1 = 'hello'
# 空串
str2 = ()
# 双引号字符串
str2 = "hello world"
print(str1,str2)
# 三引号字符串，多行字符串
str3 = '''hello world
hello 2024
'''
print(str3)
str4 = """hello 2025
hello 2025
"""
print(str4)
print('=' * 20)

# 字符串运算
str1 = 'hello python'
str2 = 'hello world'
# 字符串加法
str3 = str1 + str2
print(str3)
# 字符串乘法
str3 = str2 * 3
print(str3)
# str3 = str2 + 2
print(str3)
print('=' * 20)

# 字符串的索引
str1 = 'hello python'
print(str1[0],str1[-1])