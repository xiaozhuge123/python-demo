class Player(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

mia = Player('Mia', 20, 'male')
print(mia.name)
mia.height = 180
print(mia.__dict__)

tom = Player('Tom', 25, 'female')
print(tom.name)
print(tom.__dict__)