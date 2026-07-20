# Декоратор с аргументами. Напиши декоратор, который принимает количество попыток.
# Если декорируемая функция падает с ошибкой, декоратор должен попробовать запустить её
# снова указанное количество раз, прежде чем окончательно выкинуть исключение.

def retry(max_tries):
    def deco(func):
        def wrapper():
            temp = 0
            while temp != max_tries:
                try:
                    result = func()
                except:
                    temp += 1
                else:
                    return result
            raise AssertionError(f'Функция не смогла запуститься за {temp} попыток')
        return wrapper
    return deco

@retry(3)
def greeting():
    return

print(greeting())
