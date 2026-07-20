# Декоратор с аргументами. Напиши декоратор, который делает искусственную паузу (например, time.sleep(2))
# перед выполнением функции. Количество секунд паузы должно передаваться в сам декоратор как параметр.
import time

def timer(second):
    def deco(func):
        def wrapper():
            time.sleep(second)
            return func()
        return wrapper
    return deco

@timer(1)
def greeting():
    return 'Hello'

print(greeting())
greeting_value = timer(2)(greeting)()
print(greeting_value)