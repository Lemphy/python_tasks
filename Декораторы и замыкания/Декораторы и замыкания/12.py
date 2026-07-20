# Создай несколько декораторов: @bold, @italic, @underline. Они должны оборачивать возвращаемую строковую
# строку в соответствующие HTML-теги (<b>...</b>, <i>...</i>, <u>...</u>).

def bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

def italic(func):
    def wrapper():
        return f'<i>{func()}</i>'
    return wrapper

def underline(func):
    def wrapper():
        return f'<u>{func()}</u>'
    return wrapper

def text():
    return 'Hello'

text_variable = bold(italic(underline(text)))
print(text_variable())