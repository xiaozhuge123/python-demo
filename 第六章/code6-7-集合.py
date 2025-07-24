# 创建集合
s1 = set()
s2 = {1,2,3,4}
print(s1)
print(set([1,2,3,4,5])) # 通过列表创建
print(set((1,2,3,4,5,6))) # 通过元组创建
print(set('hello')) # 通过字符串创建
print(set({"name":"zs","age":90})) # 通过字典创建

# 作用：列表去重
li1 = [1,2,4,2,1,3,5,4,2,4,6,4,6,5,7,5,3,54,4,3,2,2]
s4 = set(li1)
print(s4)
li2 = list(s4)
print(li2)
print('*' * 20)

# 添加
# 添加不可变元素
s1.add(5)
print(s1)
# s1.add([5,6]) 不能添加列表
# print(s1)
s1.add((6,5,6,7,3)) # 可以添加元组
print(s1)

s1 = {1,2,3,4}
s1.update([5,6])
s1.update((8,9))
s1.update('hello')
s1.update({'name':'zs','age':90}) # 只会把字典的键添加进集合
print(s1)
# s1.update(6) 不能插入一个数字元素

# 删除
s6 = set([1,2,3,4,5])
data = s6.pop()
print(data,s6)

# s6.remove(6)
s6.remove(4)
print(s6)

s6.discard(2)
print(s6)
s6.discard(7)
print(s6)

# 元素个数
print(len(s6))

# 成员操作
print(2 in s6)

# 交集与并集
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)

# 遍历
s = set([1,2,3,4,5])
for key in s:
    print(key)
print('*' * 20)
for index,key in enumerate(s):
    print(index,key)







