class Dongwu(object):
    def speak(self):
        print('动物的叫声')

class Cat(Dongwu):
    def speak(self):
        print('喵喵')

class Dog(Dongwu):
    def speak(self):
        print('汪汪')

def speak(object):
    object.speak()

dw = Dongwu()
kitty = Cat()
dog = Dog()
speak(dw)
speak(dog)
speak(kitty)