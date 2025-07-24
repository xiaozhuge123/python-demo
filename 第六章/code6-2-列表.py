name_list = ['zhangsan', 'lisi','wangwu']

list1 = []
list2 = [10,9,1.23,True,'zhangsan']
list3 = list()
list4 = list('hello world')
print(list4)
print(list2)

# 列表操作
# 列表相加
li4 = [1,2,3,4]
li5 = [4,5,6,7]
li6 = li4 + li5
print(li6)

# 列表相乘
li7 = [7,8,9]
li8 = li7 * 3
print(li7)
print(li8)

# 成员判断
li9 = [1,2,3]
print(1 in li9)
print(2 not in li9)
print('*' * 20)

# 取值
li10 = [1,2,3,4,6]
num = li10[2]
print(num)
# print(li10[9])
li11 = [1,2,4,6,7]
li11.append(8)
print(li11)

print(li11[3])
print(li11[-1])
li11[2] = 90
print(li11)

print(li11[1:3])
print(li11[:2])
print(li11[1:])

# 列表修改
li11[3] = 89
print(li11)
print('*' * 20)

# 遍历
words = ['good','nice','cool','handsome']
for word in words:
    print(word)
print('*' * 20)
for word,index in enumerate(words):
    print(word,index)
print('*' * 20)

# 分数统计
score = [70,40,60,90,80,20,45]
# for score in score:
#     print(score)
total = 0
for i in score:
    if i >= 80:
        total += 1
print('分数在80分以上的人数有%d人' % total)
print('*' * 20)
score.sort(reverse=True)
for i,v in enumerate(score):
    print('第%d名的同学，成绩是%d' % (i + 1,v))
print('*' * 20)
# 遍历列表的下标和元素
words = ['good','nice','cool','handsome']
for index,word in enumerate(words):
    print(index,word)
print('*' * 20)
# 二维列表遍历
l1 = [[1,2,3],[2,3,5,6],[3,56,76,7]]
for item in l1:
    print(item)
    for value in item:
        print(value)
    print('')
print('*' * 20)

# 二维列表
li12 = [[1,2,3],[4,5,6],[7,8,9]]
print(li12[1][1])
print('*' * 20)

a = []
for i in range(4):
    a.append([1,2,3,4.5])
print(a)
print('*' * 20)

# 列表的函数操作
# 增加元素 append(obj)
li1 = [1,2,3,4,5]
li1.append(6)
li1.append([7,8,9])
print(li1)
print('*' * 20)

li1.append(40)
li1[len(li1):len(li1)] = [50]
print(li1)
li1.append([68,90])
print(li1)
print('*' * 20)

li2 = [1,2,3,4,5]
li2.extend([6,7,8,9])
print(li2)
print('*' * 20)
print(li1 + li2)

# 删除元素
value = li1.pop()
print(value)
pop = value.pop()
print(pop)
print(value)

li1.pop(2)
print(li1)

print('*' * 20)
li1.remove(5)
print(li1)
# li1.remove(600)
print(li1)
print('*' * 20)
del li1[0]
print(li1)
del li1[0:2]
print(li1)
li1.clear()
print(li1)
print('*' * 20)

# 查找元素
li1 = [1,2,3,4,5]
li__index = li1.index(4, 1, 4)
print(li__index)
li1.extend([6,7,8,9,1,23,2,1,23,2,3,1,12,2,3,4,4,322,2,2,3,4,2])
print(li1)
count = li1.count(1)
print(count)
count = li1.count(345)
print(count)
print('*' * 20)

# 列表反转
li1.reverse()
print(li1)
print('*' * 20)

# 插入元素
li3 = [1,2,3,4,5]
li3.insert(1,6)
print(li3)
li3.insert(2,-7)
print(li3)

li3.insert(0,[1,2,3,5,6])
print(li3)
print('*' * 20)

li4 = [1,2,3,4,5]
data = li4.pop()
print(data,li4)

li5 = [1,2,3,4,5,6,7,21,3,4,45,4]
li5.remove(3)
print(li5)

li4.clear()
print(li4)

value = li5.count(4)
print(value)

print(li5.index(2))
# print(li5.index(1243))

print(max(li5))
print(min(li5))

li5.sort()
print(li5)
print('*' * 20)

str1 = 'hello world'
li15 = list(str1)
print(li15)
print('*' * 20)

a = [1,2,3,4,5,6]
b = a
print(id(a),id(b))
print(a == b)
print(a is b)
print('*' * 20)

c = [1,2,34,45,[1,243,5,6,7]]
d = c
print(c == d)
print(c is d)
c[4][2] = 900
print(c)
print(d)
print('*' * 20)

# 浅拷贝
from copy import copy
a = [1,2,3,4,5,6]
b = copy(a)
print(id(a),id(b))
print(a == b)
print(a is b)
c = [1,2,3,[4,5,6]]
d = copy(c)
print(id(c),id(d))
print(c == d)
print(c is d)
print(id(c[2]),id(d[2]))
print(c[2] == d[2])
print(c[2] is d[2])
print('*' * 20)
# 深拷贝
from copy import deepcopy
a = [1,2,3,4,5,6]
b = deepcopy(a)
print(id(a),id(b))
print(a == b)
print(a is b)
print('*' * 20)
c = [1,2,3,[4,5,6]]
d = deepcopy(c)
print(id(c),id(d))
print(c == d)
print(c is d)
print(id(c[2]),id(d[2]))
print(c[2] == d[2])
print(c[2] is d[2])




























