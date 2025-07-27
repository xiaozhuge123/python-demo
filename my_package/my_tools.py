import random
# 生成一个随机字母组成的列表
a = []
n = 5
for i in range(20):
    s = ''
    for j in range(n):
        value = random.randint(65, 90)
        s += chr(value)
    a.append(s)

# 随机生成大小写字符串
def create_char(flag = True):
    if flag:
        return random.randint(ord('A'), ord('Z'))
    else:
        return random.randint(ord('a'), ord('z'))

def create_str(length):
    s = ''
    for i in range(length):
        s += chr(create_char(random.choice([True, False])))
    return s

def str_list(length,length_list):
    a = []
    for i in range(length):
        a.append(create_str(length_list))
    return a

print(str_list(5,6))