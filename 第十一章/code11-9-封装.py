class User:
    def __init__(self,name,age):
        self._name = name # 受保护的变量
        self.__age = age # 私有变量

    # 获取私有变量
    @property
    def age(self):
        return self.__age
    # 修改变量
    @age.setter
    def age(self,age):
        if age > 18:
            self.__age = age
        else:
            raise Exception('年龄必须大于18岁')

mia = User('mia',18)
print(mia.__dict__)
print(mia._name)
print(mia._User__age)
# print(mia.__age)
print(mia.age)
mia.age = 28
print(mia.age)

