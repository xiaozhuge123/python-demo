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

infos = {'name':'zhangsan','age':16,'gender':'男','level':'青铜'}
if Player.isvalide(**infos):
    mia = Player('mia',20,'女','青铜')
    print(mia.__dict__)