# Декоратор @double_it
# Условие: Напишите декоратор, который удваивает результат работы функции.
# Если функция возвращает число, оно должно умножиться на 2. Если строку — она должна повториться дважды.

def double_it(func):
    def wrapper():
        return func() * 2
    return wrapper

@double_it
def value():
    return 8

print(value())