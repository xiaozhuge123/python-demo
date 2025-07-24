# 字符串运算
str3 = "hello python"
str4 = "hello world"
# 字符串加法（字符串拼接）
str5 = str3 + str4
print("str5= %s" %str5)

# 字符串乘法（重复字符串）
str6 = str3 * 3
print("str6= %s" %str6)

# 成员判断
str7 = "hello word"
print("wo" in str7)

str1 = '天要下⾬，娘要嫁⼈，由他去吧'
print(str1[0],str1[-1])

str1 = '天要下⾬，娘要嫁⼈，由他去吧'
print(len(str1))

# 4.字符串截取（切⽚）
str1 = '123456'
print(str1[0:2]) #'12'
print(str1[1:]) #'23456'
print(str1[::2]) #'135'
print(str1[:]) #'123456'
print(str1[::-1]) #'654321'

s='hello python'
for i in s:
    print(i)

s = input('请输⼊⼀个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
 if c.isalpha():
    letters += 1
 elif c==' ':
    space += 1
 elif c.isdigit():
    digit += 1
 else:
    others += 1
print ('char = %d,space = %d,digit = %d,others = %d' %
(letters,space,digit,others))

str1 = "abc"
str2 = "ab"
print(str1 > str2)








