# Напишите фабрику декораторов prefix, которая принимает строку-префикс.
# Декоратор, который она возвращает, должен добавлять этот префикс к результату выполнения декорируемой функции.
# Декорируемая функция должна возвращать строку. Декоратор должен принимать один аргумент p (строку-префикс).
from typing import Callable
from functools import wraps

def prefix(arg: str) -> Callable:
    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args,**kwargs) -> str:
            result = arg + func(*args,**kwargs)
            return result
        return wrapper
    return deco

@prefix("[LOG]: ")
def get_status(code):
    return f'Status code is {code}'

print(get_status(200))
print(get_status(404))