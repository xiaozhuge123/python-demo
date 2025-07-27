def add(a,b):
    return a + b

def sub(*args):
    result = 0
    for arg in args:
        result += arg ** 2
    return result

author = 'jack'