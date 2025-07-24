# 列表组合，将两个列表拼接为一个列表
# 直接使用+号
list1 = [43,65,76,2,12,34,45]
list2 = [1,2,3,4,5]
print(list1 + list2)

# 列表重复
print(list1 * 2)

# 成员操作
list3 = [1,2,3,4,5,'hello','good']
print('hello' in list3)
print(8 not in list3)

# 切片
print(list1[0:3])
print(list1[:3])
print(list1[:])
print(list1[::2])
print(list1[::-1])
print(list1[3::-1])
print(list1[-1:-3:-1])
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))