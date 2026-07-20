# Создай декоратор, который выводит в консоль имя вызываемой функции и все
# аргументы (args и kwargs), с которыми она была вызвана.
from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Имя вызываемой функции: {func.__name__}\n'
              f'Аргументы args: {args}, kwargs: {kwargs}')
        tmp = func(*args)
        return tmp
    return wrapper

def function(*args):
    for i in args:
        print(i, end = ' ')

function = deco(function)
print(function(1,2,3,4))

