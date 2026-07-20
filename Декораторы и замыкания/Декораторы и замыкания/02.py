# @greetings
# Создай декоратор, который перед запуском функции выводит в консоль
# фразу "Логирование: функция начинает работу", а после завершения — "Логирование: функция завершила работу".

def greeting(func):
    def wrapper():
        print('Логирование: функция начинает работу.')
        result = func()
        print('Логирование: функция завершила работу.')
        return result
    return wrapper


def function():
    print('Работа функции..')

function = greeting(function)
function()