class Player(object):
    number = 0
    levels = ['青铜', '白银', '黄金', '钻石', '王者'] # 类变量
    # 构造方法
    def __init__(self, name, age, gender,level): # 实例变量
        self.name = name
        self.age = age
        self.gender = gender
        Player.number += 1
        if level not in Player.levels:
            raise Exception('等级不在范围内')
        else:
            self.level = level

    # 实例方法
    def get_level(self):
        print(self.level,self.name,self.age,self.gender)

    # 实例方法
    def get_wuqi_info(self,wuqi):
        self.wuqi = wuqi

    # 实例方法
    def show_wuqi(self):
        return self.wuqi.get_wuqi()

    # 类方法
    @classmethod
    def get_Player_numbers(cls):
        print('注册了%d人' %cls.number)

    # 静态方法
    @staticmethod
    def isvalide(**keywords):
        if keywords.get('age') >= 18:
            return True
        else:
            print('年龄不能小于18')

class VIP(Player):
    money = 100

    def __init__(self, name, age, gender, level,coin):
        Player.__init__(self, name, age, gender, level)
        self.coin = coin

    def de(self, coin):
        self.coin = coin

    def get_level(self):
        print(self.level,self.name,self.age,self.gender,self.coin)

mia = VIP('mia',24,'女','青铜',2000)
mia.get_level()
print(mia.coin)
print(VIP.money)
mia.de(200)
print(mia.coin)