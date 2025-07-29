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

    def get_wuqi(self):
        for k,v in self.__dict__.items():
            print(k,v)

mia = Player('Mia', 20, 'male','青铜')
mia.get_level()
dao = wuqi('火焰刀',1000,'青铜')
mia.get_wuqi_info(dao)
mia.show_wuqi()