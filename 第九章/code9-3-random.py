import random
from my_package import my_tools
a = random.random()
print(a)
b = random.randint(1, 100)
print(b)

# 获取list中的随机元素
list1 = [1,2,3,4,5,6,7,8]
print(list1[random.randint(0, len(list1)-1)])
print(random.choice(list1))
print(random.choice('hello'))
# 打乱list顺序
random.shuffle(list1)
print(list1)
print('*' * 20)

# 生成一个随机字母组成的列表
# a = []
# n = 5
# for i in range(20):
#     s = ''
#     for j in range(n):
#         value = random.randint(65, 90)
#         s += chr(value)
#     a.append(s)
# print(a)
str_list = my_tools.str_list(5, 6)
print(str_list)

create_str = my_tools.create_str(4)
print(create_str)
print('*' * 20)

# 石头剪刀布游戏
from my_package import my_game
my_game.game1()

my_game.guess_num(1,100)
