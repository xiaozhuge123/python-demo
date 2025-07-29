class Player(object):
    number = 0
    levels = ['青铜', '白银', '黄金', '钻石', '王者']
    def __init__(self, name, age, gender,level):
        self.name = name
        self.age = age
        self.gender = gender
        Player.number += 1
        if level not in Player.levels:
            raise Exception('等级不在范围内')
        else:
            self.level = level

    def get_level(self):
        print(self.level,self.name,self.age,self.gender)

    def get_wuqi_info(self,wuqi):
        self.wuqi = wuqi

    def show_wuqi(self):
        return self.wuqi.get_wuqi()

    # 类方法
    @classmethod
    def get_Player_numbers(cls):
        print('注册了%d人' %cls.number)

class wuqi(object):
    wuqis = []
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
        wuqi.wuqis.append(self)

    def get_wuqi(self):
        for k,v in self.__dict__.items():
            print(k,v)

    # 类方法
    @classmethod
    def get_max_shanghai(cls):
        shanghai = 0
        for wq in cls.wuqis:
            if wq.shanghai > shanghai:
                shanghai = wq.shanghai
        return shanghai

dao = wuqi('火焰刀',1000,'青铜')
jian = wuqi('青竹风云剑', 10000, '青铜')
ji = wuqi('方天画集', 1000, '黄金')
shanghai = wuqi.get_max_shanghai()
print(shanghai)

mia = Player('mia',20,'女','青铜')
tom = Player('tom',18,'男','白银')
jack = Player('jack',28,'男','黄金')
Player.get_Player_numbers()