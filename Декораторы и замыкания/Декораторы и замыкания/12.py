# Создай несколько декораторов: @bold, @italic, @underline. Они должны оборачивать возвращаемую строковую
# строку в соответствующие HTML-теги (<b>...</b>, <i>...</i>, <u>...</u>).

def bold(func):
    def wrapper(text: str):
        return f'<b>{func(text)}</b>'
    return wrapper

def italic(func):
    def wrapper(text:str):
        return f'<i>{func(text)}</i>'
    return wrapper

def underline(func):
    def wrapper(text:str):
        return f'<u>{func(text)}</u>'
    return wrapper

@bold
@italic
@underline
def greeting(text):
    return f'Hello, {text}'

print(greeting('Mykhailo'))

# Аналогично:
# greeting_decorated = bold(italic(underline(greeting)))
# print(greeting_decorated('Mykhailo'))