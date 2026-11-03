# Декоратор с аргументами. Напиши декоратор, который делает искусственную паузу (например, time.sleep(2))
# перед выполнением функции. Количество секунд паузы должно передаваться в сам декоратор как параметр.
import time
from typing import Callable

def timer(seconds) -> Callable:
    def deco(func) -> Callable:
        def wrapper(*args,**kwargs) -> Callable:
            time.sleep(seconds)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return deco

@timer(1) # задержка 1 секунд
def greeting(name: str) -> str:
    return 'Hello, ' + name

print(greeting('Mykhailo_1'))
greeting_deco = timer(2)(greeting)('Mykhailo_2')
# задержка 3 секунды у greeting_deco потому что вызываем уже декорированую функцию greeting с таймером 1,
# потом еще дополнительно сверху добавляем 2 секунды
print(greeting_deco)