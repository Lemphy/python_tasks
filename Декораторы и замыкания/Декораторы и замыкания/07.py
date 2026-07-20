# Если применить обычный декоратор, оригинальное имя функции (__name__) и её
# документация (__doc__) заменяются на данные внутренней функции-обертки.
# Используй functools.wraps, чтобы исправить это поведение.
from functools import wraps

def preserve_metadata(func):
    @wraps(func)
    def wrapper():
        temp = func.__name__, func.__doc__
        return temp
    return wrapper

def greeting():
    """Документация .. """
    return

greeting = preserve_metadata(greeting)
print(greeting())
