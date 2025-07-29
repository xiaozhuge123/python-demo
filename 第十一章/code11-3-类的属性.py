class Player(object):
    number = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Player.number += 1

mia = Player('Mia', 20, 'male')
print(mia.__dict__)
print('第%d个人注册' % Player.number)

tom = Player('Tom', 25, 'female')
print(tom.__dict__)
print('第%d个人注册' % Player.number)

# 定义一个武器类
class wuqi(object):
    numbers = 0
    max_shanghai = 10000
    levels = ['青铜','白银','黄金','钻石','王者']
    def __init__(self, name, shanghai, level):
        self.name = name
        self.shanghai = shanghai
        self.level = level
        wuqi.numbers += 1
        if shanghai > wuqi.max_shanghai:
            raise Exception('伤害值不能高于10000')
        if level not in wuqi.levels:
            raise Exception('等级不在范围内')
try:
    dao = wuqi('火焰刀',1000,'青铜')
    print(dao.__dict__)
    jian = wuqi('青竹风云剑', 10000, '青铜')
    print(jian.__dict__)
    ji = wuqi('方天画集', 1000, '铂金')
    print(ji.__dict__)
except Exception as e:
    print(e)


