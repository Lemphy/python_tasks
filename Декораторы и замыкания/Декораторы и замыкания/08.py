# Создай декоратор, который сохраняет результаты выполнения функции в словарь.
# Если функция вызывается с теми же аргументами повторно, она должна возвращать готовый результат из кэша,
# а не вычислять его заново.

def cache_result(func):
    storage = {5 : 25}
    def wrapper(value):
        if value not in storage:
            print('Функция была вызвана!')
            storage[value] = func(value)
            return storage[value]
        else:
            print('Функция не была вызвана!')
            return storage[value]
    return wrapper

@cache_result
def to_square(value):
    return value ** 2

for i in range(3,6):
    print(to_square(i))