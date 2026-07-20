# Создай декоратор, который ожидает, что декорируемая функция возвращает строку,
# и приводит эту строку к верхнему регистру (UPPERCASE).

def upper_deco(func):
    def wrapper():
        temp: str = func()
        return temp.upper()
    return wrapper


def function():
    return 'абвг123'

function = upper_deco(function)
print(function())