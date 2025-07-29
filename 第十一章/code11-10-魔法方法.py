class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f'{self._name}, age: {self._age}'

    def __add__(self, other):
        return self._name + other._name

    def __eq__(self, other):
        return self._age == other._age

mia = User('mia',28)
tom = User('tom',24)
print(str(mia) + str(tom))
print(mia.__add__(tom))
print(mia.__eq__(tom))