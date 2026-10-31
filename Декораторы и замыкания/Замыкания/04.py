# Валидатор пароля по длине
# Создай функцию make_length_checker(min_length). Она должна возвращать функцию,
# которая принимает строку (пароль) и возвращает True, если её длина больше или равна min_length,
# и False в противном случае.
from typing import Callable

def make_length_checker(min_length: int) -> Callable:
    def wrapper(arg: str) -> bool:
        return len(arg) >= min_length
    return wrapper

func = make_length_checker(6)
print(func('python_top'))