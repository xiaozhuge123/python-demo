stu = {'name':'zhangsan','age':10,'gender':'male'}
print(stu)

stu1 = {}
stu2 = dict()
stu3 = {'name':'zhangsan','age':10,'gender':'male'}
stu4 = dict(a=1,b=2)
print(stu4)
stu5 = dict([('a',1),('b',2)])
print(stu5)
stu6 = dict({'name':'zhangsan','age':10,'gender':'male'})
print(stu6)

# 访问字典
stu7 = {"name": "xiaoming", "age": 18, "sex": "男", "height": 173.5, "weight":80, "id": 1}
print(stu7['name'])
# print(stu7['money'])
print(stu7.get('age'))
print(stu7.get('money'))
money = stu7.get("money")
if money:
    print("money = %d"%money)
else:
    print("没有money属性")
result = stu7.get("score",1)  # 如果没有这个键，返回默认值1，不会报错
print(result)

# 添加元素
stu7['money'] = 90
print(stu7)

# 删除元素
value = stu7.pop('age')
print(value)
print(stu7)

del stu7['sex']
print(stu7)
stu7.clear()
print(stu7)
del stu7
# print(stu7)

# 常用方法
# 存储多个学生的成绩
dict1 = {"jack":90,"zs":99,"ls":87}
print(dict1)

# 字典合并
a = {1:'hello'}
b = {2:'world'}
a.update(b)
print(a)

# 遍历
dict2 = {"jack":90,"zs":99,"ls":87}
# 方式一
for key in dict2:
    print(key,dict2[key])

# 方式二
values = dict2.values()
print(values)
for value in values:
    print(value)

# 方式三
for key,value in dict1.items():
    print(key,value)

# 方式四
for index,key in enumerate(dict1):
    print(index,key,dict1[key])

# 获取键值对的个数
print(len(dict2))

# 成员操作
print('age' in dict2)















