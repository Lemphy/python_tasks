# Напиши декоратор, который проверяет, что аргумент функции является целым числом (int).
# Если передано что-то другое, декоратор должен выводить ошибку TypeError.

def type_check(func):
    def wrapper(arg):
        if isinstance(arg, int):
            return func(arg)
        else:
            raise TypeError
    return wrapper

def my_function(value):
    return value ** 2

my_function = type_check(my_function) # получаем объект обертку и переприсваиваем
print(my_function(5)) # вызываем полученный объект обертку
